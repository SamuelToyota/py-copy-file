def copy_file(command: str) -> None:
    parts = command.strip().split()

    # Validar comando
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Comando inválido. Use o formato: cp origem destino")

    src, dst = parts[1], parts[2]

    # Não fazer nada se os nomes forem iguais
    if src == dst:
        return

    # Copiar conteúdo
    with open(src, "r", encoding="utf-8") as file_in, open(dst, "w", encoding="utf-8") as file_out:
        file_out.write(file_in.read())
