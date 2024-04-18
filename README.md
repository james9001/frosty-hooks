# Frosty Hooks

My custom pre-commit hooks for various tech stacks. Just super simple stuff.

## Principle/s of Frosty Hooks

There seems to be some discordance in the concept of pre-commit: should the hooks expect the tools to be available in $PATH already, or should they be self-installing and even self-contained (not polluting $PATH with random new tool installations)?

Well, Frosty Hooks takes a firm stance: they're expected to already be there in $PATH.
