# Task 5 — Async Array Function Variants

Цей репозиторій містить реалізації асинхронного аналога функції `map` з використанням:
- Callback (через `asyncio.create_task`)
- Promise (через `async def` та `await`)
- Приклади використання з `async/await`
- Демонстраційні приклади
- Механізм переривання (cancellation) через спільний прапор

## Файли:
- `async_map.py` — реалізації функцій `async_map_callback` та `async_map_promise`
- `test_async_map.py` — тести для обох варіантів (виводять результати в консоль)

## Як запустити:
```bash
python test_async_map.py
