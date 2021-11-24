# Hack Hours - 2021-11-24

## The State Machine pattern

Oftentimes when programming, we end up with some gnarly, tangled, hard-to-reason-about conditional logic full of if-statements that deal with some internal state. What if there was a different way to tackle the problem, a design pattern that made it easier to reason about the logic?

[Material](./1_stateful_objects)

## Design by "Wishful Thinking"

Code is a language used to plan things. In SICP this is called "design by [wishful thinking](https://wiki.c2.com/?WishfulThinking)". In other places, this is referred to as "top-down" design.

You start by pretending that you have a library of functions that do exactly what you want. You then write your program using those functions, and then go back and fill in the details afterwards. https://www.youtube.com/watch?v=amf5lTZ0UTc&t=3501s

[Material](./2_wishful_thinking)

## References

- [Advanced Programming with Python](https://www.dabeaz.com/advprog.html)
- [The structure and interpretation of computer programs (SICP)](https://mitpress.mit.edu/sites/default/files/sicp/index.html)
  - [MIT OpenCourseware Video lectures](https://www.youtube.com/watch?v=2Op3QLzMgSY&list=PL7F7312C6EAAD5D22)
  - [David Beazley's SICP course](https://www.dabeaz.com/sicp.html)
- [Boundaries - Gary Bernhardt](https://www.destroyallsoftware.com/talks/boundaries)
- [pytest-recording](https://github.com/kiwicom/pytest-recording) and [vcrpy](https://vcrpy.readthedocs.io/en/latest/usage.html#record-modes)