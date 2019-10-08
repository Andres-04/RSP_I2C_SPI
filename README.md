# Protocolos de comunicaciones para intercomunicar dispositivos IoT
Luego de aprender acerca de los diferentes tipos de protocolos usados en la industria para envio de datos, llevamos a cabo el siguiente taller con el fin de afianzar los conocimientos obtenidos en clase.

Objetivos requeridos
===========
- Afianzar los conceptos básicos asociados a Internet de las Cosas (IoT).
- Familiarizarse con los protocolos típicos de comunicaciones entre dispositivos IoT vía cables.
- Desarrollar dos aplicaciones sencillas para transferir comandos entre dos Raspberry Pi para encender y apagar un actuador LED utilizando I2C y SPI.
- Presentar las aplicaciones funcionando correctamente.

Materiales utilizados
===========
- 1 PC
- 1 Raspberry Pi
-1 Arduino UNO
- 1 actuador LED
- 1 protoboard y cables.
- 1 resistor de 330 ohmios.
- 1 pulsador

Cuadro comparativo entre I2C y SPI
===========
Con el fin de familiarizarnos mejor con las ventajas entre estos dos tipos de protocolos realizamos la siguiente tabla
![Tabla](https://raw.githubusercontent.com/Andres-04/RSP_I2C_SPI/master/Imagen1.png?token=ANCIDMYLPXRNFSXGBOCDOPC5TPNIU)

Configurar I2C en Raspberry PI
=
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.

Configurar I2C en Arduino UNO
=
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.

Configurar SPI en Raspberry PI
=
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.

Configurar SPI en Arduino UNO
=
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.

Implementación del protocolo I2C
=
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.

-Diagrama de bloques implementado:
Imagen

-Criterios de diseño
Los criterios de diseño que implementamos fue que la solución final debia conectar entre si, una Raspberry PI y un Arduino UNO mediante el protocolo I2C y encender un LED desde el Arduino UNO y recibiendo esta orden de la Raspberry PI configurada como maestro en este caso.

-Esquematico del circuito
Imagen

-Código utilizado
Maestro:
Codigoooooo
Esclavo:
Codigoooooo

Implementación del protocolo SPI
=
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.

-Diagrama de bloques implementado:
Imagen

-Criterios de diseño
Los criterios de diseño que implementamos fue que la solución final debia conectar entre si, una Raspberry PI y un Arduino UNO mediante el protocolo I2C y encender un LED desde el Arduino UNO y recibiendo esta orden de la Raspberry PI configurada como maestro en este caso.

-Esquematico del circuito
Imagen

-Código utilizado
Maestro:
Codigoooooo
Esclavo:
Codigoooooo



