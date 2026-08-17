import asyncio

async def tarefa(nome, duracao):
    print(f"Tarefa [{nome}] inciando...")
    await asyncio.sleep(duracao)
    print(f"Tarefa [{nome}] terminou...")

async def main():
    await asyncio.gather(
        tarefa(1, 3),
        tarefa(2, 9),
        tarefa(3, 0)
        )

    await tarefa(4, 0)

if __name__ == "__main__":
    asyncio.run(main())