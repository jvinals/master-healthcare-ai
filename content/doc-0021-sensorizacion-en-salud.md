---
id: DOC-0021
title: Sensorización en Salud
version: '1.0'
status: Draft
authors: []
created: '2026-06-08'
updated: '2026-06-08'
tags:
- telemedicina
- salud
related: []
source: raw_data/master-training/Formación/Asignatura de Telemedicina.- Grado de Ingeniería Informática
  Biomédica/Sensorización en Salud.pptx
source_sha256: b94a2561aac156184e2b63bd9263dc91a05b07bd8ce8f560398e3497d560cf98
canonical: false
family_id: fam-sensorizacion-en-salud
supersedes: []
superseded_by: ''
language: es
category: asignatura-telemedicina
n_pages: 20
---

# Sensorización en Salud

> Generado automáticamente desde `raw_data/master-training/Formación/Asignatura de Telemedicina.- Grado de Ingeniería Informática Biomédica/Sensorización en Salud.pptx` por `scripts/ingest.py`. Revisar metadatos en el frontmatter y en `data/document-registry.yaml`.

## Diapositiva 1

Ingeniería Informática Biomédica
Telemedicina
Sensorización en Salud

## Diapositiva 2

Ingeniería Informática Biomédica
Telemedicina
Sensorización Biomédica: Introducción
Definición: Uso de sensores para medir parámetros fisiológicos en pacientes.
Importancia en telemedicina: Monitoreo remoto, diagnóstico y prevención.
Objetivos de la sesión:
Conocer los tipos de sensores biomédicos.
Entender el procesamiento de señales.
Aplicar conceptos en casos prácticos.
Los sensores biomédicos permiten medir parámetros fisiológicos en pacientes, facilitando el monitoreo remoto y el diagnóstico en telemedicina. Esta sesión busca comprender los tipos de sensores, cómo se procesan las señales y aplicar estos conceptos en casos prácticos, mejorando la atención a distancia.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 3

Ingeniería Informática Biomédica
Telemedicina
Clasificación General de Sensores Biomédicos
Sensores físicos: Medición de variables físicas (e.g., temperatura, presión).
Sensores químicos: Detección de compuestos químicos (e.g., glucosa, pH).
Sensores biológicos: Respuesta a estímulos biológicos (e.g., enzimas, células).
Aplicaciones principales:
Monitorización de signos vitales.
Diagnóstico de enfermedades crónicas.
Seguimiento en tratamientos médicos.
Los sensores biomédicos se clasifican en tres categorías principales: físicos, que miden variables como la temperatura y la presión; químicos, que detectan compuestos como la glucosa; y biológicos, que responden a estímulos como enzimas o células. Estos sensores son esenciales en el monitoreo de signos vitales, el diagnóstico de enfermedades crónicas y el seguimiento de tratamientos médicos, mejorando la precisión y la eficiencia en la atención sanitaria.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 4

Ingeniería Informática Biomédica
Telemedicina
Sensores Físicos
Sensores de presión: Medición de presión arterial, presión intracraneal.
Sensores de temperatura: Monitoreo de temperatura corporal, fiebre.
Sensores de movimiento: Acelerómetros, giroscopios para actividad física y rehabilitación.
Sensores de flujo: Medición del flujo de aire o líquido, utilizados en respiradores y equipos de ventilación.
Ejemplos y casos de uso:
Monitorización de signos vitales en pacientes críticos.
Seguimiento de actividad física en telemedicina.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 5

Ingeniería Informática Biomédica
Telemedicina
Sensores Químicos
Sensores de pH: Medición de acidez en sangre, fluidos corporales.
Sensores de glucosa: Control de niveles de glucosa en pacientes diabéticos.
Sensores de oxígeno: Determinación de niveles de oxígeno en tejidos.
Sensores de electrolitos: Monitorización de iones como sodio, potasio, y calcio.
Aplicaciones clínicas:
Control de diabetes, equilibrio ácido-base, monitorización de oxígeno en sangre.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 6

Ingeniería Informática Biomédica
Telemedicina
Sensores Biológicos
Biosensores enzimáticos: Detectan la actividad de enzimas en procesos metabólicos.
Sensores inmunológicos: Detección de antígenos y anticuerpos en respuestas inmunes.
Sensores basados en ADN: Identificación de secuencias genéticas específicas.
Tendencias actuales: Diagnóstico personalizado, biosensores portátiles, análisis rápido de enfermedades.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 7

Ingeniería Informática Biomédica
Telemedicina
Tecnologías de Adquisición de Datos
Sistemas de adquisición analógica: Recogen señales físicas en forma continua.
Conversión analógico-digital: Transformación de señales continuas en datos digitales.
Tasas de muestreo: Frecuencia con la que se capturan los datos.
Resolución y precisión: Exactitud y nivel de detalle de los datos adquiridos.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 8

Ingeniería Informática Biomédica
Telemedicina
Arquitectura de Sistemas de Adquisición
Componentes principales: Sensores, conversores A/D, procesadores, almacenamiento.
Flujo de datos: Desde el sensor hasta el sistema de procesamiento.
Almacenamiento: Local o en la nube.
Transmisión en tiempo real: Datos enviados a plataformas remotas para monitorización.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 9

Ingeniería Informática Biomédica
Telemedicina
Procesamiento de Señales Biomédicas
Tipos de señales biomédicas:
ECG (Electrocardiograma): Medición de la actividad eléctrica del corazón.
EEG (Electroencefalograma): Registro de la actividad eléctrica cerebral.
EMG (Electromiograma): Medición de la actividad muscular.
Presión arterial: Monitoreo de la fuerza de la sangre contra las arterias.
SpO2 (Saturación de oxígeno): Nivel de oxígeno en la sangre.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 10

Ingeniería Informática Biomédica
Telemedicina
Análisis de Señales
Dominio del tiempo: Evaluación de las señales en función del tiempo.
Dominio de la frecuencia: Análisis de las frecuencias presentes en la señal.
Transformadas (Fourier, Wavelets): Métodos para descomponer señales complejas.
Extracción de características: Identificación de patrones clave en la señal.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 11

Ingeniería Informática Biomédica
Telemedicina
Filtrado de Señales
Tipos de ruido en señales biomédicas: Interferencias, ruido muscular, ruido eléctrico.
Filtros analógicos vs digitales: Diferencias en implementación y aplicaciones.
Filtros FIR e IIR: Tipos de filtros digitales con diferentes características.
Técnicas de suavizado: Eliminación de fluctuaciones indeseadas en la señal.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 12

Ingeniería Informática Biomédica
Telemedicina
Eliminación de Interferencias
Interferencia de red eléctrica (50/60 Hz): Ruido generado por fuentes eléctricas.
Artefactos de movimiento: Distorsiones debidas al movimiento del paciente o del equipo.
Interferencia electromagnética: Ruido causado por dispositivos electrónicos cercanos.
Técnicas de cancelación adaptativa: Métodos dinámicos para reducir interferencias.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 13

Ingeniería Informática Biomédica
Telemedicina
Sensores Wearables
Tecnologías actuales: Sensores de ritmo cardíaco, SpO2, acelerómetros.
Integración en dispositivos: Relojes inteligentes, pulseras de actividad, ropa inteligente.
Desafíos técnicos: Duración de la batería, precisión de las mediciones, conectividad.
Consideraciones de diseño: Comodidad, usabilidad, seguridad de los datos.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 14

Ingeniería Informática Biomédica
Telemedicina
Validación y Calibración
Métodos de validación: Comparación con estándares médicos y pruebas clínicas.
Procesos de calibración: Ajuste de los dispositivos para garantizar precisión.
Control de calidad: Procedimientos para mantener la fiabilidad del dispositivo.
Normativas y estándares: Cumplimiento con regulaciones como FDA, CE, ISO.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 15

Ingeniería Informática Biomédica
Telemedicina
Consideraciones Clínicas
Precisión requerida: Exactitud en las mediciones para un diagnóstico fiable.
Fiabilidad y robustez: Capacidad de los dispositivos para funcionar correctamente en diversas condiciones.
Seguridad del paciente: Protección contra riesgos asociados al uso de dispositivos.
Certificaciones médicas: Aprobaciones regulatorias (FDA, CE) necesarias para uso clínico.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 16

Ingeniería Informática Biomédica
Telemedicina
Futuras Tendencias
Miniaturización: Dispositivos más pequeños, portátiles y discretos.
Sensores implantables: Monitoreo continuo dentro del cuerpo.
Tecnologías emergentes: Biosensores avanzados, nanotecnología.
Integración con IA: Diagnóstico predictivo y análisis avanzado.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 17

Ingeniería Informática Biomédica
Telemedicina
Preguntas y Discusión

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 18

Ingeniería Informática Biomédica
Telemedicina
Casos Prácticos
Caso Práctico 1: Diseño de un Sistema de Monitorización con Sensores Wearables
Objetivo: Crear un sistema de monitorización continua de salud.
Componentes clave: Sensores de ritmo cardíaco, SpO2, acelerómetros.
Tecnología de transmisión: Bluetooth, Wi-Fi, 4G/5G.
Plataforma de análisis: Integración con aplicaciones móviles y plataformas en la nube.
Desafíos: Batería, precisión, seguridad de datos.

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 19

Ingeniería Informática Biomédica
Telemedicina
Casos Prácticos
Caso Práctico 2: Procesamiento de Datos de ECG en Tiempo Real
Objetivo: Capturar, procesar y analizar datos de ECG en tiempo real.
Componentes: Sensores de ECG, software de procesamiento, algoritmos de detección de arritmias.
Análisis de la señal: Filtrado de ruido, detección de picos QRS, ritmo cardíaco.
Desafíos: Precisión en tiempo real, eliminación de artefactos, alertas automáticas.
https://youtu.be/d4Fw9RNjZnw?si=3LNW8q7GbMzKarFx

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.


## Diapositiva 20

Ingeniería Informática Biomédica
Telemedicina
Gracias

> **Notas:** ¿Qué es la Telemedicina?
Definición formal de telemedicina
Telemedicina se define como la provisión de servicios de salud a distancia mediante el uso de tecnologías de la información y comunicación (TIC). Implica la evaluación, diagnóstico, tratamiento, seguimiento y educación a través de medios digitales, permitiendo a los profesionales de la salud atender a los pacientes sin la necesidad de estar físicamente presentes.
Aplicaciones en el ámbito de la salud
La telemedicina tiene una amplia gama de aplicaciones en el sector salud, entre las cuales se incluyen:
	•	Teleconsulta: Permite a los pacientes consultar con médicos y especialistas a través de videollamadas, chats o llamadas telefónicas, eliminando la necesidad de desplazamientos.
	•	Telediagnóstico: Los médicos pueden recibir datos médicos (como imágenes, resultados de pruebas de laboratorio, etc.) y hacer diagnósticos sin que el paciente esté presente físicamente.
	•	Telemonitorización: Los pacientes con enfermedades crónicas o condiciones que requieren seguimiento continuo pueden ser monitoreados en tiempo real desde sus hogares, mediante dispositivos conectados que envían datos a los profesionales de la salud.
	•	Telesalud pública: La telemedicina se utiliza para promover la salud pública, incluyendo campañas de vacunación, educación en salud y control de brotes de enfermedades a gran escala.
	•	Tele-educación en salud: Profesionales de la salud y pacientes pueden recibir formación continua o capacitación a través de plataformas en línea, mejorando la difusión del conocimiento médico.
Diferencias con otros conceptos como e-Salud y m-Salud
	•	e-Salud (Salud Electrónica): Es un concepto más amplio que incluye la telemedicina, pero también abarca otras aplicaciones de las TIC en la salud, como la historia clínica electrónica (EHR), los sistemas de información hospitalaria (HIS), y la salud digital en general. La e-Salud implica la integración de tecnologías digitales en todos los aspectos del cuidado de la salud.
	•	m-Salud (Salud Móvil): Es una subcategoría de la e-Salud que se centra en el uso de dispositivos móviles y aplicaciones para la salud. La m-Salud incluye el uso de smartphones, tabletas, y otros dispositivos portátiles para monitorear la salud, acceder a información médica, y mejorar la comunicación entre pacientes y proveedores de salud. La m-Salud es parte de la telemedicina cuando se utiliza para consultas y monitorización a distancia, pero su alcance se extiende más allá de esto.
