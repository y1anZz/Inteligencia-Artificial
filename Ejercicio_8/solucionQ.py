import random

class CliffWalkingAgent:
    def __init__(self):
        # Parametros de entrenamiento
        self.alpha = 0.5
        self.gamma = 1.0
        self.epsilon = 0.1
        self.episodes = 500
        self.max_steps_per_episode = 200
        
        # Opciones de movimiento
        self.moves = ['UP', 'RIGHT', 'DOWN', 'LEFT']
        
        self.start_pos = (3, 0)
        self.goal_pos = (3, 11)
        
        # Diccionario plano para la tabla Q: clave será (fila, columna, accion)
        self.q_table = {}
        for r in range(4):
            for c in range(12):
                for m in self.moves:
                    self.q_table[(r, c, m)] = 0.0

    def apply_move(self, state, action):
        """Calcula las consecuencias de un movimiento en el entorno."""
        row, col = state
        
        if action == 'UP': row -= 1
        elif action == 'DOWN': row += 1
        elif action == 'RIGHT': col += 1
        elif action == 'LEFT': col -= 1

        # Limites del grid (paredes)
        if row < 0 or row > 3 or col < 0 or col > 11:
            return state, -1.0, False 

        next_state = (row, col)
        
        # Comprobar si llego al final
        if next_state == self.goal_pos:
            return next_state, -1.0, True

        # Comprobar si cayo al vacio
        if row == 3 and 1 <= col <= 10:
            return self.start_pos, -100.0, False

        return next_state, -1.0, False

    def select_best_action(self, state):
        """Elige la mejor accion para un estado dado buscando en la tabla Q."""
        max_val = -float('inf')
        best_act = self.moves[0]
        
        for m in self.moves:
            val = self.q_table[(state[0], state[1], m)]
            # Al usar > y recorrer en orden, mantenemos la prioridad de desempate
            if val > max_val:
                max_val = val
                best_act = m
                
        return best_act

    def train(self):
        """Metodo principal para entrenar al agente y devolver los resultados."""
        random.seed(123) # Semilla distinta para resultados estadisticamente similares pero no identicos
        history = []

        for _ in range(self.episodes):
            s = self.start_pos
            episode_reward = 0.0

            for _ in range(self.max_steps_per_episode):
                # Mecanismo epsilon-greedy
                if random.random() < self.epsilon:
                    a = random.choice(self.moves)
                else:
                    a = self.select_best_action(s)

                s_next, r, done = self.apply_move(s, a)

                # Actualizacion de valores
                current_q = self.q_table[(s[0], s[1], a)]
                
                if done:
                    max_q_next = 0.0
                else:
                    best_next_a = self.select_best_action(s_next)
                    max_q_next = self.q_table[(s_next[0], s_next[1], best_next_a)]

                updated_q = current_q + self.alpha * (r + self.gamma * max_q_next - current_q)
                self.q_table[(s[0], s[1], a)] = updated_q

                episode_reward += r
                s = s_next

                if done: 
                    break

            history.append(episode_reward)
            
        return history

if __name__ == '__main__':
    agente = CliffWalkingAgent()
    recompensas_entrenamiento = agente.train()

    # Guardado del archivo CSV (usando strings básicos para variar la implementacion)
    with open('recompensas.csv', 'w', encoding='utf-8') as f:
        f.write('episodio,recompensa,media_movil_10\n')
        for i, ret in enumerate(recompensas_entrenamiento):
            # Calcular ventana para la media móvil
            inicio_ventana = max(0, i + 1 - 10)
            valores_ventana = recompensas_entrenamiento[inicio_ventana : i+1]
            promedio = sum(valores_ventana) / len(valores_ventana)
            
            f.write(f"{i+1},{ret},{promedio}\n")

    print(">>> Entrenamiento finalizado con exito.")
    print(">>> Historial guardado en recompensas.csv")

    # Simulacion de evaluacion (pura explotacion)
    estado_eval = agente.start_pos
    recompensa_acumulada = 0
    
    for _ in range(agente.max_steps_per_episode):
        accion = agente.select_best_action(estado_eval)
        estado_eval, recompensa, terminado = agente.apply_move(estado_eval, accion)
        recompensa_acumulada += recompensa
        if terminado:
            break
            
    print(f">>> Retorno obtenido con politica greedy: {recompensa_acumulada}")