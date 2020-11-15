import asyncio
def run(coroutine):
    if coroutine is str:
        return
    try:
        # pass
        coroutine.send(None)
    except StopIteration as e:
        return e.value
# def greet_(name: str):
#     if name is None:
#         return
#     return 'hi ' + name
async def _greet(name: str):
    return 'hi ' + name
fu = [_greet]
for f in fu:
    print(run(f('respects')))
