# Análisis PEAS de Agentes Inteligentes

---

## 1. Asistente virtual de voz

- **Performance (Rendimiento):** Precisión en el reconocimiento de voz (tasa de error de palabras), relevancia de la respuesta, tiempo de latencia, satisfacción del usuario, tasa de éxito al completar tareas comandadas (ej. encender luces, programar alarmas).
- **Environment (Entorno):** Entorno doméstico o móvil, voces humanas (diferentes acentos), ruidos de fondo, conexión a internet, dispositivos inteligentes interconectados.
- **Actuators (Actuadores):** Altavoz (emisión de voz sintética, alarmas, música), pantalla (si el dispositivo cuenta con una), APIs de servicios web (enviar mensajes, consultar clima, agendar en calendario), controladores IoT (encender/apagar luces).
- **Sensors (Sensores):** Micrófono (captura de audio), reloj del sistema, estado de conexión de red, GPS (si es un dispositivo móvil).


---

## 2. Robot aspirador doméstico

- **Performance:** Porcentaje de superficie limpiada, cantidad de polvo recogido, minimización de tiempo de limpieza, evitación de obstáculos y caídas, retorno exitoso a la base de carga, minimización de ruido.
- **Environment:** Suelos de una vivienda, distribución de muebles, presencia de escaleras, movimiento de mascotas y personas, distintos tipos de superficie (alfombras, madera).
- **Actuators:** Ruedas motrices (dirección y velocidad), motor de succión, cepillos giratorios y laterales, altavoz pequeño (para emitir pitidos o alertas de estado).
- **Sensors:** Sensores de choque (parachoques), láser (LIDAR) o cámaras para mapeo y distancia, sensores de desnivel (infrarrojos para evitar escaleras), sensor de suciedad, medidor de nivel de batería.


---

## 3. Sistema de recomendación de streaming

- **Performance:** Tasa de clics (CTR) en las recomendaciones, tiempo total de retención/visualización, aumento en la tasa de suscripciones o renovaciones, diversidad del catálogo mostrado.
- **Environment:** Plataforma digital, inmensa base de datos de contenido (películas/canciones), perfiles e historial de millones de usuarios simultáneos.
- **Actuators:** Interfaz gráfica (mostrar carruseles personalizados, ordenar elementos en pantalla), envío de notificaciones push o correos electrónicos promocionales.
- **Sensors:** Entradas de la interfaz web/app (clics, reproducciones, pausas, abandonos, "me gusta"), tiempo de visualización, consultas en la barra de búsqueda, hora del día, datos del perfil (edad, región).


---

## 4. Vehículo autónomo en ciudad

- **Performance:** Seguridad (cero colisiones), cumplimiento estricto de las normas de tráfico, minimización del tiempo de viaje al destino, confort del pasajero (aceleración/frenado suaves), eficiencia de consumo de energía.
- **Environment:** Calles urbanas, tráfico vehicular denso, peatones, ciclistas, semáforos, señales de tráfico, condiciones climáticas variables (lluvia, sol).
- **Actuators:** Volante (control de dirección), pedal de aceleración, pedal de freno, luces (faros, intermitentes), claxon, sistema de infoentretenimiento.
- **Sensors:** Cámaras de video, LIDAR (percepción de profundidad 3D), radar, receptor GPS, acelerómetros, sensores ultrasónicos de proximidad, micrófono (para detectar sirenas de emergencia).


---

## 5. Agente de trading algorítmico en bolsa

- **Performance:** Maximización del retorno de inversión (ROI) a corto o largo plazo, minimización del riesgo (volatilidad), reducción de costos por transacción (comisiones), cumplimiento de métricas de margen.
- **Environment:** Mercados financieros globales, libros de órdenes (order books), noticias financieras, competidores (otros agentes e inversores humanos).
- **Actuators:** API del broker o mercado (enviar órdenes de compra, enviar órdenes de venta, cancelar órdenes activas, ajustar límites de stop-loss).
- **Sensors:** Flujo de datos del mercado en tiempo real (precios, volumen, profundidad del libro), feeds de noticias (APIs de Bloomberg/Reuters), reloj atómico, indicadores macroeconómicos.


---

## 6. Sistema de diagnóstico médico asistido por IA

- **Performance:** Precisión del diagnóstico (minimización de falsos positivos y falsos negativos), reducción del tiempo de análisis, utilidad y claridad de la justificación proporcionada al médico tratante.
- **Environment:** Historiales clínicos electrónicos (EHR), bases de datos de imágenes médicas, síntomas descritos por el paciente, retroalimentación del médico humano.
- **Actuators:** Interfaz de pantalla (mostrar lista de posibles diagnósticos con porcentajes de probabilidad, resaltar con mapas de calor áreas anómalas en una radiografía), sugerir pruebas de laboratorio adicionales.
- **Sensors:** Interfaz de entrada de datos (archivos DICOM de imágenes médicas, resultados de laboratorio en texto/números, síntomas ingresados, datos biométricos del paciente).


---

## 7. Dron de inspección de infraestructura

- **Performance:** Cobertura de inspección del 100% de la superficie objetivo, precisión en la detección de anomalías (grietas, corrosión, fugas), vuelo seguro sin colisiones, minimización del tiempo de vuelo para conservar batería.
- **Environment:** Espacio exterior tridimensional industrial (puentes, torres eléctricas, tuberías), corrientes de viento, clima (lluvia, luz solar directa), aves, cables colgantes.
- **Actuators:** Motores y hélices (control de altitud, pitch, roll, yaw), estabilizador de cámara (gimbal pan/tilt), control de zoom del lente, luces de iluminación.
- **Sensors:** Cámaras de alta resolución (RGB, térmica o infrarroja), GPS/GLONASS, IMU (giroscopios, acelerómetros, magnetómetro), altímetro barométrico, LIDAR o sensores ultrasónicos de proximidad, monitor de voltaje de batería.


---

## 8. Agente jugador de ajedrez

- **Performance:** Porcentaje de partidas ganadas o empatadas, maximización del rating Elo, cumplimiento del tiempo límite por movimiento (reloj de ajedrez).
- **Environment:** Tablero de ajedrez virtual de 64 casillas, 32 piezas en juego, reglas estrictas de movimiento, oponente (humano u otra IA).
- **Actuators:** Interfaz digital (mover una pieza de la casilla X a la casilla Y, coronar un peón, declarar jaque mate o reclamar tablas por repetición).
- **Sensors:** Interfaz receptora (estado completo del tablero y ubicación exacta de cada pieza), lectura del reloj de ajedrez propio y del oponente, recepción de la jugada enemiga.
