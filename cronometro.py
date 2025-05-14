import time

def formatar_tempo(segundos):
    minutos = segundos // 60
    segundos_restantes = segundos % 60
    return f"{minutos:02d}:{segundos_restantes:02d}"

def cronometro():
    print("=== Cronômetro Simples ===")
    print("Comandos: 'start' para iniciar, 'pause' para pausar, 'reset' para zerar, 'exit' para sair.")

    tempo_decorrido = 0
    rodando = False
    ultimo_tempo = None

    while True:
        comando = input("Digite um comando: ").strip().lower()

        if comando == "start":
            if not rodando:
                rodando = True
                ultimo_tempo = time.time()
                print("Cronômetro iniciado.")
            else:
                print("Cronômetro já está rodando.")
        elif comando == "pause":
            if rodando:
                rodando = False
                tempo_decorrido += int(time.time() - ultimo_tempo)
                print(f"Cronômetro pausado em {formatar_tempo(tempo_decorrido)}.")
            else:
                print("Cronômetro não está rodando.")
        elif comando == "reset":
            tempo_decorrido = 0
            rodando = False
            ultimo_tempo = None
            print("Cronômetro zerado.")
        elif comando == "exit":
            if rodando:
                tempo_decorrido += int(time.time() - ultimo_tempo)
            print(f"Cronômetro finalizado em {formatar_tempo(tempo_decorrido)}. Até mais!")
            break
        else:
            print("Comando inválido. Use 'start', 'pause', 'reset' ou 'exit'.")

        if rodando:
            tempo_atual = tempo_decorrido + int(time.time() - ultimo_tempo)
            print(f"Tempo atual: {formatar_tempo(tempo_atual)}")

if __name__ == "__main__":
    cronometro()
