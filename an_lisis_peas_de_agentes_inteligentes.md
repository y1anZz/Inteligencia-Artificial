# Análisis PEAS de Agentes Inteligentes

Este documento contiene la descripción del entorno de tarea (esquema **PEAS**) y la clasificación del entorno para 8 aplicaciones distintas de agentes inteligentes.

---

## 1. Asistente virtual de voz
*(ej. Siri, Alexa o Google Assistant)*

- **Performance (Rendimiento):** Precisión en el reconocimiento de voz (tasa de error de palabras), relevancia de la respuesta, tiempo de latencia, satisfacción del usuario, tasa de éxito al completar tareas comandadas (ej. encender luces, programar alarmas).
- **Environment (Entorno):** Entorno doméstico o móvil, voces humanas (diferentes acentos), ruidos de fondo, conexión a internet, dispositivos inteligentes interconectados.
- **Actuators (Actuadores):** Altavoz (emisión de voz sintética, alarmas, música), pantalla (si el dispositivo cuenta con una), APIs de servicios web (enviar mensajes, consultar clima, agendar en calendario), controladores IoT (encender/apagar luces).
- **Sensors (Sensores):** Micrófono (captura de audio), reloj del sistema, estado de conexión de red, GPS (si es un dispositivo móvil).

> **Justificación del entorno:** Es *parcialmente observable* porque el agente no conoce el estado mental del usuario ni todo lo que ocurre en la casa. Es *estocástico* porque el ruido de fondo o la pronunciación alteran las percepciones de forma impredecible, y *dinámico* porque el entorno cambia mientras el agente procesa.

---

## 2. Robot aspirador doméstico

- **Performance:** Porcentaje de superficie limpiada, cantidad de polvo recogido, minimización de tiempo de limpieza, evitación de obstáculos y caídas, retorno exitoso a la base de carga, minimización de ruido.
- **Environment:** Suelos de una vivienda, distribución de muebles, presencia de escaleras, movimiento de mascotas y personas, distintos tipos de superficie (alfombras, madera).
- **Actuators:** Ruedas motrices (dirección y velocidad), motor de succión, cepillos giratorios y laterales, altavoz pequeño (para emitir pitidos o alertas de estado).
- **Sensors:** Sensores de choque (parachoques), láser (LIDAR) o cámaras para mapeo y distancia, sensores de desnivel (infrarrojos para evitar escaleras), sensor de suciedad, medidor de nivel de batería.

> **Justificación del entorno:** Es *parcialmente observable* porque los muebles ocultan áreas y el mapa se descubre empíricamente. Es *dinámico* ya que las personas o mascotas pueden cruzarse en su camino durante la limpieza, y *secuencial* porque cada movimiento determina la posición futura y las opciones de navegación.

---

## 3. Sistema de recomendación de streaming
*(ej. Netflix, Spotify)*

- **Performance:** Tasa de clics (CTR) en las recomendaciones, tiempo total de retención/visualización, aumento en la tasa de suscripciones o renovaciones, diversidad del catálogo mostrado.
- **Environment:** Plataforma digital, inmensa base de datos de contenido (películas/canciones), perfiles e historial de millones de usuarios simultáneos.
- **Actuators:** Interfaz gráfica (mostrar carruseles personalizados, ordenar elementos en pantalla), envío de notificaciones push o correos electrónicos promocionales.
- **Sensors:** Entradas de la interfaz web/app (clics, reproducciones, pausas, abandonos, "me gusta"), tiempo de visualización, consultas en la barra de búsqueda, hora del día, datos del perfil (edad, región).

> **Justificación del entorno:** Es *parcialmente observable* porque el sistema desconoce el estado de ánimo real del usuario o si hay alguien más viendo la pantalla. Es *discreto* porque elige recomendaciones de un catálogo finito, y *estocástico* ya que las preferencias humanas cambian por factores externos inmedibles.

---

## 4. Vehículo autónomo en ciudad

- **Performance:** Seguridad (cero colisiones), cumplimiento estricto de las normas de tráfico, minimización del tiempo de viaje al destino, confort del pasajero (aceleración/frenado suaves), eficiencia de consumo de energía.
- **Environment:** Calles urbanas, tráfico vehicular denso, peatones, ciclistas, semáforos, señales de tráfico, condiciones climáticas variables (lluvia, sol).
- **Actuators:** Volante (control de dirección), pedal de aceleración, pedal de freno, luces (faros, intermitentes), claxon, sistema de infoentretenimiento.
- **Sensors:** Cámaras de video, LIDAR (percepción de profundidad 3D), radar, receptor GPS, acelerómetros, sensores ultrasónicos de proximidad, micrófono (para detectar sirenas de emergencia).

> **Justificación del entorno:** Es *continuo* y *dinámico* porque la posición, velocidad y el estado del tráfico cambian en tiempo real de forma fluida. Es altamente *estocástico* porque el comportamiento exacto de otros conductores y peatones es impredecible, y *parcialmente observable* debido a puntos ciegos u oclusiones por otros vehículos.

---

## 5. Agente de trading algorítmico en bolsa

- **Performance:** Maximización del retorno de inversión (ROI) a corto o largo plazo, minimización del riesgo (volatilidad), reducción de costos por transacción (comisiones), cumplimiento de métricas de margen.
- **Environment:** Mercados financieros globales, libros de órdenes (order books), noticias financieras, competidores (otros agentes e inversores humanos).
- **Actuators:** API del broker o mercado (enviar órdenes de compra, enviar órdenes de venta, cancelar órdenes activas, ajustar límites de stop-loss).
- **Sensors:** Flujo de datos del mercado en tiempo real (precios, volumen, profundidad del libro), feeds de noticias (APIs de Bloomberg/Reuters), reloj atómico, indicadores macroeconómicos.

> **Justificación del entorno:** Es *secuencial* porque invertir capital hoy afecta las opciones de compra de mañana. Es *estocástico* por la gigantesca cantidad de variables ocultas que alteran los precios, y *parcialmente observable* porque es imposible conocer la estrategia o liquidez oculta de los demás participantes.

---

## 6. Sistema de diagnóstico médico asistido por IA

- **Performance:** Precisión del diagnóstico (minimización de falsos positivos y falsos negativos), reducción del tiempo de análisis, utilidad y claridad de la justificación proporcionada al médico tratante.
- **Environment:** Historiales clínicos electrónicos (EHR), bases de datos de imágenes médicas, síntomas descritos por el paciente, retroalimentación del médico humano.
- **Actuators:** Interfaz de pantalla (mostrar lista de posibles diagnósticos con porcentajes de probabilidad, resaltar con mapas de calor áreas anómalas en una radiografía), sugerir pruebas de laboratorio adicionales.
- **Sensors:** Interfaz de entrada de datos (archivos DICOM de imágenes médicas, resultados de laboratorio en texto/números, síntomas ingresados, datos biométricos del paciente).

> **Justificación del entorno:** Es *parcialmente observable* porque la verdadera patología biológica está oculta internamente y los síntomas/imágenes son solo observaciones indirectas. Suele considerarse *episódico* (o de horizonte muy corto) porque el diagnóstico de un paciente no afecta las reglas subyacentes para diagnosticar al siguiente paciente, y *estático* mientras se analiza el caso de forma asíncrona.

---

## 7. Dron de inspección de infraestructura

- **Performance:** Cobertura de inspección del 100% de la superficie objetivo, precisión en la detección de anomalías (grietas, corrosión, fugas), vuelo seguro sin colisiones, minimización del tiempo de vuelo para conservar batería.
- **Environment:** Espacio exterior tridimensional industrial (puentes, torres eléctricas, tuberías), corrientes de viento, clima (lluvia, luz solar directa), aves, cables colgantes.
- **Actuators:** Motores y hélices (control de altitud, pitch, roll, yaw), estabilizador de cámara (gimbal pan/tilt), control de zoom del lente, luces de iluminación.
- **Sensors:** Cámaras de alta resolución (RGB, térmica o infrarroja), GPS/GLONASS, IMU (giroscopios, acelerómetros, magnetómetro), altímetro barométrico, LIDAR o sensores ultrasónicos de proximidad, monitor de voltaje de batería.

> **Justificación del entorno:** Es *dinámico* y *continuo* por las complejas variables aerodinámicas del vuelo al aire libre en un espacio 3D. Es *estocástico* debido a las ráfagas de viento o aves inesperadas, y *parcialmente observable* porque el dron debe moverse para ver detrás de estructuras u obstáculos que bloquean la visión inicial.

---

## 8. Agente jugador de ajedrez

- **Performance:** Porcentaje de partidas ganadas o empatadas, maximización del rating Elo, cumplimiento del tiempo límite por movimiento (reloj de ajedrez).
- **Environment:** Tablero de ajedrez virtual de 64 casillas, 32 piezas en juego, reglas estrictas de movimiento, oponente (humano u otra IA).
- **Actuators:** Interfaz digital (mover una pieza de la casilla X a la casilla Y, coronar un peón, declarar jaque mate o reclamar tablas por repetición).
- **Sensors:** Interfaz receptora (estado completo del tablero y ubicación exacta de cada pieza), lectura del reloj de ajedrez propio y del oponente, recepción de la jugada enemiga.

> **Justificación del entorno:** Es *totalmente observable* porque la posición de todas las piezas siempre está a la vista. Es *determinista* (de tipo estratégico) porque las reglas establecen que cada movimiento tiene un resultado exacto sin azar (no hay dados), *discreto* (hay un número finito de casillas y opciones), y *estático*, ya que el tablero no cambia por sí solo mientras el agente está calculando su jugada.