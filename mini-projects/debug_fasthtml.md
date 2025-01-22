---
title: "Adding a Debug View for FastHTML Learning"
date: 2025-01-21
categories:
    - "mini-projects"
---

Thinking about how to teach web dev and FastHTML inspired this quick mini-project: making a debug view for FastHTML apps that renders requests and responses. Nothing fancy, but with minimal work and a bit of MonsterUI for styling I think it looks and works quite well!

![A demo site (left) and the debug page (right)](images/debug.png)

Here's how this is used in this demo app:

```python
from fasthtml.common import *
from debug import debug_wrap


app = FastHTML()
debug_wrap(app)
rt = app.route

@rt('/')
def get(): return Div(
    P('Hello World!'), 
    A('About', href='/about'), 
    Div(id='htmxtest'), 
    Button('Click me', hx_post='/test', hx_target='#htmxtest'))

@rt
def about(a:int=None): 
    return Titled('About',
        P('This is the about page'),
        A('Go back', href="/"),
        P(f'You passed a={a}') if a else None
    )

@rt('/test')
def post(): return Div('Clicked!')

serve()
```

And the entirity of debug.py:

```python
from fasthtml.common import *
from collections import deque
from monsterui.all import *
from typing import Any
import json, pprint, textwrap

updates = deque(maxlen=10)

def before(req, session):
    if '/debug' in str(req.url): return
    updates.append({
        'type': 'request',
        'method': req.method,
        'url': str(req.url),
        'session': dict(session or {}),
        'headers': dict(req.headers)
    })

def after(resp):
    resp_html = to_xml(resp)
    if not resp or 'debug' in resp_html: return
    updates.append({'type': 'response','html': resp_html})

def debug_wrap(app):

    app.before.append(before)
    app.after.append(after)

    @app.route('/debug')
    def debug_page():
        return Div(
            H3("Debugging Console", cls=TextFont.bold_sm),
            P("Requests/responses captured:"), 
            Div(id='debug_updates', hx_trigger='every 1s', hx_get='/debug_updates', hx_swap='afterbegin'),
            cls='p-4 space-y-4'
        ), Theme.orange.headers(highlightjs=True)

    @app.route('/debug_updates')
    def debug_updates_view():
        items = []
        while len(updates):
            data = updates.popleft()
            items.append(RequestCard(data) if data['type'] == 'request' else ResponseCard(data))
        if not items: return
        return Div(*items, cls='debug')

def RequestCard(data: dict[str, Any]):
    return Card(DivVStacked(
            H4("REQUEST", cls=(TextT.bold,)),
            P(f"{data.get('method')}: {data.get('url')}", cls=TextFont.muted_sm),
            DivCentered(Grid(
                DivCentered(Details(Summary('Session'), render_md("```js\n"+wrap_pformat(json.dumps(data.get('session')))+"\n```"))),
                DivCentered(Details(Summary('Headers'), render_md("```js\n"+wrap_pformat(json.dumps(data.get('headers')))+"\n```"))),
            ))
    ))

def ResponseCard(data: dict[str, Any]) -> FT:
    html_str = data.get('html') or ''
    return Card(DivVStacked(
        H4("RESPONSE", cls=(TextT.bold,)),
        render_md("```html\n"+html_str+"```")))

### For formatting json into something I can stuff in a code block, thanks AI:
class WrappingPrettyPrinter(pprint.PrettyPrinter):
    def _format(self, obj, stream, indent, allowance, context, level):
        # If it's a long string, forcibly wrap it
        if isinstance(obj, str) and len(obj) > self._width:
            # Break the string into lines of up to self._width
            wrapped_lines = textwrap.wrap(obj, self._width)
            for i, line in enumerate(wrapped_lines):
                if i > 0:
                    # Move to a new line and indent properly
                    stream.write('\n' + ' ' * indent)
                super()._format(line, stream, indent, allowance if i == 0 else 1, context, level)
        else:
            # Otherwise, do the normal pprint formatting
            super()._format(obj, stream, indent, allowance, context, level)

def wrap_pformat(obj, width=80):
    """Return a pretty-printed string where long strings are line-wrapped."""
    printer = WrappingPrettyPrinter(width=width)
    return printer.pformat(obj)
```