-- data.sql

-- Llenado de la tabla 'sintomas'
INSERT INTO sintomas (codigo_sintoma, descripcion, categoria)
VALUES
    ('S-001', 'El dispositivo no enciende', 'Alimentación'),
    ('S-002', 'Se percibe un olor a quemado', 'Sensorial'),
    ('S-003', 'Un capacitor está visiblemente hinchado o goteando', 'Inspección Visual'),
    ('S-004', 'Resistencia R10 muestra signos de quemadura (decoloración)', 'Inspección Visual'),
    ('S-005', 'Voltaje 0V en el regulador de 5V', 'Medición');

-- Llenado de la tabla 'fallos'
INSERT INTO fallos (codigo_fallo, nombre_fallo, solucion_recomendada)
VALUES
    ('F-001', 'Capacitor de entrada dañado', 'Reemplazar el capacitor C1 (100uF/25V) en la etapa de entrada. Verificar polaridad.'),
    ('F-002', 'Resistencia de protección abierta', 'Reemplazar R10 (10 Ohm 1/2W) y verificar la causa del corto circuito que la quemó.'),
    ('F-003', 'Diodo rectificador en corto', 'Reemplazar el diodo D1 (1N4007) en el puente rectificador. Verificar fusible de entrada.'),
    ('F-004', 'Regulador de voltaje dañado', 'Reemplazar el regulador U1 (LM7805). Comprobar que no haya sobrecalentamiento.'),
    ('F-005', 'Pista de PCB (circuito impreso) rota', 'Inspeccionar visualmente la placa en busca de fisuras. Reparar la pista cortada con un puente de soldadura.');

-- Llenado de la tabla 'reglas'
INSERT INTO reglas (id_fallo, id_sintoma)
VALUES
    -- Regla 1: Si no enciende (S-001) Y el capacitor está hinchado (S-003) -> Fallo F-001
    (1, 1),
    (1, 3),

    -- Regla 2: Si huele a quemado (S-002) Y la resistencia R10 está quemada (S-004) -> Fallo F-002
    (2, 2),
    (2, 4),

    -- Regla 3: Si no enciende (S-001) Y huele a quemado (S-002) -> Posiblemente Fallo F-003 (Diodo)
    (3, 1),
    -- Regla 4: Si el voltaje en el regulador es 0V (S-005) -> Fallo F-004 (Regulador dañado)
    (4, 5),

    -- Regla 5: Si el dispositivo no enciende (S-001) Y hay una pista rota (inspección visual) -> Fallo F-005
    (5, 1),
    (5, 4);


-- Llenado de la tabla 'expresiones_usuario'
INSERT INTO expresiones_usuario (frase, id_sintoma)
VALUES
    ('mi aparato no prende', 1),
    ('el circuito no funciona en absoluto', 1),
    ('huele a quemado', 2),
    ('veo un capacitor gordo', 3),
    ('la resistencia R10 está negra', 4);
