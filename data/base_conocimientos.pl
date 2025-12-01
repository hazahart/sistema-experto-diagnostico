:- dynamic verificar/1.

diagnostico(Codigo, Fallo, Solucion) :-
  regla(Codigo, Fallo, Solucion).

regla('F-001',
      'Capacitor de entrada dañado',
      'Reemplazar el capacitor en la etapa de entrada y verificar polaridad.') :-
    verificar('El dispositivo no enciende'),
    verificar('Un capacitor esta visiblemente hinchado o dañado').
regla('F-002',
      'Resistencia de protección abierta',
      'Reemplazar la resistencia y verificar la causa del corto circuito que la quemó.') :-
    verificar('Se percibe un olor a quemado'),
    verificar('La resistencia muestra signos de quemadura').
regla('F-003',
      'Diodo rectificador en corto',
      'Reemplazar el diodo rectificador y revisar el fusible de entrada.') :-
    verificar('El dispositivo no enciende'),
    verificar('Se percibe un olor a quemado').
regla('F-004',
      'Regulador de voltaje dañado',
      'Reemplazar el regulador y comprobar que no haya sobrecalentamiento.') :-
    verificar('El voltaje es de 0V en el regulador de 5V').
regla('F-005',
      'Pista de PCB rota',
      'Reparar la parte dañada con un puente de soldadura.') :-
    verificar('El dispositivo no enciende'),
    verificar('La resistencia muestra signos de quemadura').
regla('F-006',
      'Fusible de entrada fundido',
      'Reemplazar el fusible y verificar que no exista un cortocircuito posterior.') :-

    verificar('El dispositivo no enciende'),
    verificar('No hay continuidad en el fusible').
regla('F-007',
      'Cable de alimentación roto',
      'Reemplazar el cable y revisar la conexión de entrada.') :-
    verificar('El dispositivo no enciende'),
    verificar('Mover el cable provoca falsos contactos').
regla('F-008',
      'Conector flojo o sulfatado',
      'Limpiar o reemplazar el conector y resoldar si es necesario.') :-
    verificar('El equipo funciona de manera intermitente'),
    verificar('El voltaje varía al mover el conector').
regla('F-009',
      'Capacitor de desacoplo abierto',
      'Reemplazar el capacitor y revisar tensiones de alimentación.') :-
    verificar('Ruido eléctrico en la alimentación'),
    verificar('Inestabilidad en circuitos digitales').
regla('F-010',
      'Transistor de potencia en corto',
      'Reemplazar transistor y revisar etapa de carga.') :-
    verificar('El fusible se quema inmediatamente'),
    verificar('El transistor se calienta rápidamente').
regla('F-011',
      'Resistencia alterada de valor',
      'Sustituir la resistencia por una del valor correcto.') :-
    verificar('El circuito se comporta de forma anormal'),
    verificar('La resistencia marca un valor incorrecto').
regla('F-012',
      'Diodo zener abierto',
      'Reemplazar el diodo zener en la etapa reguladora.') :-
    verificar('Voltaje de referencia incorrecto'),
    verificar('La regulación es inestable').
regla('F-013',
      'Oscilador de cristal dañado',
      'Reemplazar el cristal y verificar capacitores asociados.') :-
    verificar('El microcontrolador no arranca'),
    verificar('No hay señal de reloj').
regla('F-014',
      'IC de control sobrecalentado',
      'Reemplazar el integrado y verificar consumo.') :-
    verificar('El integrado se calienta incluso sin carga'),
    verificar('El circuito se apaga por protección térmica').
regla('F-015',
      'Soldadura fría en terminal de potencia',
      'Resoldar el punto y asegurar la unión.') :-
    verificar('Falla intermitente'),
    verificar('El equipo responde al mover la placa').
regla('F-016',
      'Pista en corto por exceso de soldadura',
      'Retirar soldadura y reparar pista.') :-
    verificar('El fusible se quema'),
    verificar('Corriente excesiva en la zona afectada').
regla('F-017',
      'Inductor abierto',
      'Reemplazar el inductor.') :-
    verificar('No hay transferencia de energía en la fuente'),
    verificar('Voltaje de salida igual a 0V').
regla('F-018',
      'Sensor desconectado',
      'Reconectar o reemplazar el sensor.') :-
    verificar('Lecturas invalidas o nulas'),
    verificar('Error de calibracion').
regla('F-019',
      'Capacitor ceramico en corto',
      'Reemplazar capacitor ceramico.') :-
    verificar('Consumo excesivo'),
    verificar('Oscilacion o ruidos electricos').
regla('F-020',
      'Transformador abierto',
      'Sustituir transformador.') :-
    verificar('No hay voltaje secundario'),
    verificar('Zumbido o sobrecalentamiento').
regla('F-021',
      'Puente rectificador abierto',
      'Cambiar puente rectificador.') :-
    verificar('Salida DC con baja tension'),
    verificar('Parpadeo en circuitos').
regla('F-022',
      'Potenciometro desgastado',
      'Cambiar el potenciometro.') :-
    verificar('Saltos de valor'),
    verificar('Ruidos al girar').
regla('F-023',
      'Interruptor mecanico danado',
      'Reemplazar el interruptor.') :-
        verificar('No hace contacto'),
    verificar('Se hunde o queda flojo').
regla('F-024',
      'Refrigeracion insuficiente',
      'Limpiar ventilacion, cambiar ventilador o disipador.') :-
    verificar('Apagados termicos'),
    verificar('Componentes muy calientes').
regla('F-025',
      'Ventilador trabado o sucio',
      'Lubricar o reemplazar ventilador.') :-
    verificar('Ruido excesivo'),
    verificar('Sobrecalentamiento').
regla('F-026',
      'Fuente de alimentacion inestable',
      'Reemplazar capacitores de filtro y revisar regulador.') :-
    verificar('Voltaje de la fuente principal fluctuante o inestable').
regla('F-027',
      'Fusible se abre repetidamente',
      'Revisar cortocircuitos en la entrada y componentes en corto.') :-
    verificar('Fusible que se abre repetidamente').
regla('F-028',
      'Capacitor electrolitico hinchado',
      'Reemplazar capacitor y revisar sobretensiones.') :-
    verificar('Capacitor electrolitico hinchado o con fuga visible').
regla('F-029',
      'Componente con sobrecalentamiento',
      'Revisar sobrecarga y mejorar disipacion.') :-
    verificar('Resistencia o componente cercano a la fuente excesivamente caliente').
regla('F-030',
      'Zumbido o ruido en transformador',
      'Revisar sobrecorriente o saturacion del transformador.') :-
    verificar('Ruidos o zumbidos en transformador o fuente').
regla('F-031',
      'Interferencia en senal digital',
      'Revisar conexion a tierra y capacitores de desacoplo.') :-
    verificar('Señal digital interferida o corrompida').
regla('F-032',
      'Apagado inesperado',
      'Revisar ventilacion, disipador o sensores termicos.') :-
    verificar('Se apaga el equipo sin aviso').
regla('F-033',
      'Conexiones sulfatadas',
      'Limpiar terminales y mejorar proteccion contra humedad.') :-
    verificar('Conexiones sucias oxidadas o sulfatadas').
regla('F-034',
      'Soldaduras agrietadas en SMD',
      'Resoldar o reponer componente SMD.') :-
    verificar('Componentes SMD desprendidos o con soldadura agrietada').
regla('F-035',
      'Errores en comunicacion digital',
      'Revisar trazado, niveles de senal e interferencias.') :-
    verificar('Alta frecuencia de errores en comunicacion').
regla('F-036',
      'Fuente conmutada inestable',
      'Analizar la compensacion del lazo de control; revisar valores de componentes de lazos y optoacoplador; corregir red de compensacion.') :-
    verificar('La salida de la fuente oscila o presenta voltaje inestable'),
    verificar('La regulacion falla al cambiar carga').
regla('F-037',
      'Microcontrolador no arranca en power-up',
      'Verificar VDD minimo, linea RESET/MCLR, cristal/oscilador y temporizadores de arranque (PWRT/OST); reprogramar si es necesario.') :-
    verificar('No hay actividad del microcontrolador al aplicar energia'),
    verificar('El programa no se ejecuta').
regla('F-038',
      'Fallo por gate-drive insuficiente en MOSFET',
      'Revisar resistencia de gate, conductor de gate y reemplazar MOSFET si hay signos de degrado; asegurar drive correcto.') :-
    verificar('MOSFET se calienta o no conmuta correctamente'),
    verificar('Se detecta perdida de conmutacion o oscilaciones en la etapa de potencia').
regla('F-039',
      'Degradacion por recovery de diodo lenta',
      'Reemplazar diodos o MOSFETs por dispositivos con menor carga de recuperacion; revisar condiciones de carga baja/alta.') :-
    verificar('Fallos o sobretemperaturas en MOSFET en topologia resonante'),
    verificar('Comportamiento anomalo a baja carga').
regla('F-040',
      'Soldadura fria o agrietada',
      'Reflujo o resoldar puntos sospechosos; limpiar y reforzar soldaduras en componentes SMD/through-hole.') :-
    verificar('Fallas intermitentes al mover la placa'),
    verificar('Puntos de soldadura opacos o con grietas visibles').
regla('F-041',
      'Contaminacion en PCB (residuos conductivos)',
      'Limpiar la PCB con alcohol isopropilico; secar y verificar continuidad; aislar zonas si es necesario.') :-
    verificar('Cortos intermitentes o comportamiento erratico'),
    verificar('Residuo visible o humedad en la placa').
regla('F-042',
      'Saturacion o nucleo flojo en transformador',
      'Verificar integridad del nucleo y bobinado; reemplazar transformador o asegurar nucleo para eliminar zumbidos y saturacion.') :-
    verificar('Zumbido fuerte en transformador'),
    verificar('Distorsion en salida o calentamiento excesivo').
regla('F-043',
      'Capacitor con ESR elevado',
      'Medir ESR; reemplazar condensadores electroliticos de filtrado si ESR supera tolerancia; verificar rizado en railes.') :-
    verificar('Rizado o ripple excesivo en la salida DC'),
    verificar('Reinicios o inestabilidad bajo carga').
regla('F-044',
      'Sobrecorriente por carga en corto',
      'Desconectar carga, medir resistencia, identificar la zona en corto y reemplazar componente danado.') :-
    verificar('La fuente entra en proteccion inmediatamente'),
    verificar('El consumo sube bruscamente al conectar la carga').
regla('F-045',
      'Oscilacion en amplificador operacional',
      'Revisar red RC de compensacion, verificar conexion en retroalimentacion y reemplazar amplificador si es necesario.') :-
    verificar('Hay ruido u oscilacion en la salida del operacional'),
    verificar('La tension cambia sin motivo aparente').
regla('F-046',
      'Entradas flotantes en microcontrolador',
      'Activar resistencias pull-up o pull-down, revisar configuracion del firmware.') :-
    verificar('El microcontrolador detecta entradas falsas'),
    verificar('Las entradas digitales cambian sin accion del usuario').
regla('F-047',
      'Mal contacto en bornera',
      'Ajustar, limpiar o reemplazar bornera; verificar torque adecuado.') :-
    verificar('La carga conecta y desconecta de forma intermitente'),
    verificar('Mover la bornera provoca apagones').
regla('F-048',
      'Diodo Schottky degradado',
      'Reemplazar diodo Schottky; revisar condiciones de corriente inversa y temperatura.') :-
    verificar('El voltaje cae mas de lo esperado en la salida'),
    verificar('El diodo se calienta en exceso').
regla('F-049',
      'Sensor de temperatura defectuoso',
      'Comprobar alimentacion y referencia; reemplazar sensor.') :-
    verificar('Lecturas de temperatura erroneas o poco realistas'),
    verificar('La proteccion termica se activa sin razon').
regla('F-050',
      'Fallo por humedad en conectores',
      'Secar, limpiar y aislar conectores; aplicar protector contra humedad.') :-
    verificar('El equipo falla despues de exposicion a humedad'),
    verificar('Corrosion leve o gotas visibles en conectores').
regla('F-051',
      'Bateria con corto interno',
      'Reemplazar la bateria y verificar circuito de carga.') :-
    verificar('La bateria se calienta rapidamente'),
    verificar('Voltaje en bornes cae abruptamente').
regla('F-052',
      'Falla en oscilador interno del microcontrolador',
      'Ajustar calibracion OSCCAL o seleccionar frecuencia externa.') :-
    verificar('El MCU ejecuta codigo mas lento o mas rapido de lo normal'),
    verificar('Funciones temporizadas dejan de operar correctamente').
regla('F-053',
      'Fallo en conversor ADC',
      'Revisar referencia de voltaje, ruido en tierra y reemplazar ADC si es necesario.') :-
    verificar('Lecturas digitales inestables'),
    verificar('ADC cambia valores sin variacion real').
regla('F-054',
      'Interferencia en sensor analogico',
      'Agregar filtrado RC, blindaje o mejorar trazado de PCB.') :-
    verificar('Lectura analogica con ruido excesivo'),
    verificar('Valores varian segun cercania a cables de potencia').
regla('F-055',
      'Regulador lineal sobrecalentado',
      'Agregar disipacion o reemplazar por regulador conmutado.') :-
    verificar('Regulador demasiado caliente'),
    verificar('Voltaje de salida cae al aumentar la carga').
regla('F-056',
      'MOSFET con fuga en estado off',
      'Reemplazar MOSFET y revisar aislamiento del gate.') :-
    verificar('La carga recibe voltaje incluso apagada'),
    verificar('Hay fuga entre drenador y fuente').
regla('F-057',
      'Microcontrolador danado por ESD',
      'Reemplazar MCU y agregar proteccion ESD en pines sensibles.') :-
    verificar('Entradas digitales fallan despues de tocar el equipo'),
    verificar('Comportamiento erratico despues de descarga estatica').
regla('F-058',
      'Reinicio por ruido en alimentacion',
      'Agregar capacitores de desacoplo y ferritas.') :-
    verificar('El equipo reinicia al activar motores o cargas'),
    verificar('Voltaje cae brevemente al cambiar la carga').
regla('F-059',
      'Corto intermitente por tornillo suelto',
      'Ajustar tornillos y aislar componentes cercanos.') :-
    verificar('Golpes o vibraciones causan fallas'),
    verificar('Corto desaparece al mover la carcasa').
regla('F-060',
      'Fallo en puente H',
      'Reemplazar transistores del puente y revisar deadtime.') :-
    verificar('Motor no gira o se queda trabado'),
    verificar('Calentamiento de transistores en puente H').
regla('F-061',
      'Memoria flash corrupta',
      'Reprogramar firmware o reemplazar chip de memoria.') :-
    verificar('Firmware no arranca'),
    verificar('Datos almacenados aparecen dañados').
regla('F-062',
      'Bobina saturada',
      'Reemplazar inductor por uno de mayor corriente.') :-
    verificar('Fuente genera ruido a altas cargas'),
    verificar('Voltaje cae cuando la carga aumenta').
regla('F-063',
      'Rele con contactos sulfatados',
      'Lijar contactos o reemplazar rele.') :-
    verificar('El rele activa pero no conduce'),
    verificar('Se escucha clic pero carga no enciende').
regla('F-064',
      'Driver de motor quemado',
      'Reemplazar driver y revisar corriente del motor.') :-
    verificar('Motor vibra pero no gira'),
    verificar('El driver se calienta de inmediato').
regla('F-065',
      'Fallo en proteccion termica',
      'Revisar termistores NTC/PTC o sensor de temperatura.') :-
    verificar('Equipo no enciende por proteccion'),
    verificar('Proteccion termica se activa sin razon').
regla('F-066',
      'Zumbido por soldadura deficiente en fuente',
      'Resoldar transformador e inductores.') :-
    verificar('Zumbido cambia al presionar la PCB'),
    verificar('Ruido aumenta al aumentar carga').
regla('F-067',
      'Cristal mal acoplado',
      'Revisar capacitores de carga y reemplazar cristal.') :-
    verificar('Microcontrolador arranca solo a veces'),
    verificar('Reloj interno se detiene o es inestable').
regla('F-068',
      'Capacitor de arranque defectuoso',
      'Reemplazar capacitor de arranque en SMPS.') :-
    verificar('Fuente intenta arrancar y se apaga'),
    verificar('Arranques repetitivos en ciclos cortos').
regla('F-069',
      'Sensor Hall danado',
      'Reemplazar sensor Hall y revisar conexiones.') :-
    verificar('No detecta campo magnetico'),
    verificar('Lecturas saltan o se vuelven cero').
regla('F-070',
      'Capacitor de filtro con fuga',
      'Reemplazar capacitor de filtro y revisar rizado de la fuente.') :-
    verificar('Rizado excesivo en la salida'),
    verificar('Voltaje cae al aumentar la carga').
regla('F-071',
      'Selector de voltaje danado',
      'Reemplazar el selector o corregir posicion incorrecta.') :-
    verificar('Equipo no enciende en cierto modo'),
    verificar('Selector se siente flojo o suelto').
regla('F-072',
      'Terminal de sensor con soldadura rota',
      'Resoldar terminal y asegurar conexion mecanica.') :-
    verificar('Sensor deja de funcionar al mover el cable'),
    verificar('Lectura del sensor se pierde intermitentemente').
regla('F-073',
      'Diodo flyback danado',
      'Reemplazar diodo y revisar bobina inductiva.') :-
    verificar('Transistor asociado se calienta demasiado'),
    verificar('Circuito de bobina genera ruido fuerte').
regla('F-074',
      'Fallo en convertidor boost',
      'Reemplazar MOSFET, inductor o diodo del boost.') :-
    verificar('Voltaje de salida menor al esperado'),
    verificar('Circuito intenta subir voltaje pero se colapsa').
regla('F-075',
      'Sensor optico sucio',
      'Limpiar lente o reemplazar sensor optico.') :-
    verificar('El sensor no detecta objetos'),
    verificar('Lectura disminuye con el tiempo').
regla('F-076',
      'Bobina con espiras en corto',
      'Reemplazar bobina y revisar temperatura de operacion.') :-
    verificar('Inductor se calienta sin carga'),
    verificar('Fuente pierde eficiencia').
regla('F-077',
      'Switch tactil fallando',
      'Reemplazar el switch tactil.') :-
    verificar('Boton responde solo a veces'),
    verificar('Presionar fuerte es necesario para activar').
regla('F-078',
      'Encoder mecanico desgastado',
      'Reemplazar encoder o lubricar mecanismo interno.') :-
    verificar('Saltos al girar encoder'),
    verificar('Valores cambian de manera incorrecta').
regla('F-079',
      'Falta de capacitor de desacoplo',
      'Agregar capacitor cerca del IC.') :-
    verificar('Reinicios al conectar carga'),
    verificar('Inestabilidad en señales digitales').
regla('F-080',
      'PWM inestable',
      'Revisar temporizador del MCU y capacitores asociados.') :-
    verificar('La senal PWM cambia sin control'),
    verificar('Frecuencia inconsistentes en la salida').
regla('F-081',
      'Cable de datos roto',
      'Reemplazar cable y verificar continuidad de hilos.') :-
    verificar('Comunicacion intermitente'),
    verificar('No hay respuesta del dispositivo').
regla('F-082',
      'PCB doblada o fracturada',
      'Reemplazar PCB o reparar pistas danadas.') :-
    verificar('Equipo falla al presionar la placa'),
    verificar('Zonas flexionadas en PCB').
regla('F-083',
      'Terminal de tierra desconectada',
      'Restablecer conexion de tierra y asegurar contacto.') :-
    verificar('Circuito presenta ruido excesivo'),
    verificar('Fallas aleatorias en funcionamiento').
regla('F-084',
      'Resistencia fusible abierta',
      'Reemplazar resistencia fusible y revisar corriente.') :-
    verificar('No hay voltaje en etapa secundaria'),
    verificar('Componente muestra color quemado').
regla('F-085',
      'Optoacoplador saturado',
      'Reemplazar optoacoplador y revisar corrriente de LED interno.') :-
    verificar('Salida del optoacoplador es demasiado baja'),
    verificar('Fuente no regula correctamente').
regla('F-086',
      'Driver de LED fallando',
      'Reemplazar driver o revisar corriente de salida.') :-
    verificar('LEDs parpadean'),
    verificar('Intensidad luminosa baja o inestable').
regla('F-087',
      'Sensor magnetico invertido',
      'Reinstalar sensor en la orientacion correcta.') :-
    verificar('Sensor no detecta iman'),
    verificar('Lecturas opuestas al movimiento real').
regla('F-088',
      'Capacitor ceramico fracturado',
      'Reemplazar capacitor ceramico y revisar montaje.') :-
    verificar('Oscilaciones en circuitos de alta frecuencia'),
    verificar('Capacitor presenta grietas visibles').
regla('F-089',
      'SSR danado internamente',
      'Reemplazar relay de estado solido.') :-
    verificar('Salida permanece abierta o cerrada siempre'),
    verificar('Resistencia interna demasiado alta').
regla('F-090',
      'Bucle de masa',
      'Reorganizar tierras y eliminar lazo de retorno largo.') :-
    verificar('Ruido en audio o mediciones'),
    verificar('Voltaje de referencia fluctua').
regla('F-091',
      'Cristal contaminado',
      'Limpiar PCB y reemplazar cristal.') :-
    verificar('Reloj deja de oscilar aleatoriamente'),
    verificar('Microcontrolador se frena o acelera sin razon').
regla('F-092',
      'Pista de retorno rota',
      'Resoldar o puentear pista de retorno.') :-
    verificar('Lecturas inexactas en ADC'),
    verificar('Fluctuaciones al energizar cargas').
regla('F-093',
      'Sonda defectuosa',
      'Reemplazar sonda o recalibrar.') :-
    verificar('Mediciones incorrectas'),
    verificar('Valores estan fuera de rango').
regla('F-094',
      'Reset por ruido externo',
      'Agregar capacitor de filtro y mejorar blindaje.') :-
    verificar('Reinicio inesperado del MCU'),
    verificar('Fallas coinciden con cargas inductivas').
regla('F-095',
      'Capacitor de reloj degradado',
      'Reemplazar capacitor y verificar frecuencia.') :-
    verificar('Reloj pierde estabilidad'),
    verificar('Frecuencia varia con la temperatura').
regla('F-096',
      'Pin Vref desconectado',
      'Reconectar Vref y agregar desacoplo.') :-
    verificar('ADC presenta mediciones erraticas'),
    verificar('Referencia fluctua en reposo').
regla('F-097',
      'Boost sincronizado fallando',
      'Revisar sincronizacion y reemplazar MOSFET.') :-
    verificar('Boost genera ruido excesivo'),
    verificar('Voltaje sube y cae repetidamente').
regla('F-098',
      'Falta de diodo flyback',
      'Agregar diodo de proteccion en bobinas.') :-
    verificar('Transistor de salida se quema al accionar carga'),
    verificar('Se escuchan chispas o golpes electricos').
regla('F-099',
      'I2C sin resistencias pullup',
      'Agregar resistencias pullup a SDA y SCL.') :-
    verificar('No hay comunicacion I2C'),
    verificar('Lineas SDA/SCL quedan siempre en bajo').
regla('F-100',
      'Optoacoplador sin corriente suficiente',
      'Ajustar resistencia limitadora o cambiar optoacoplador.') :-
    verificar('Salida del optoacoplador es muy debil'),
    verificar('La etapa de potencia no responde con fiabilidad').
