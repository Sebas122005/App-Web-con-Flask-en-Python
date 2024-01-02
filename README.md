## Flask-WTF:
En resumen, Flask-WTF es una valiosa extensión para Flask que simplifica la creación y validación de formularios en aplicaciones web, ayudando a proteger contra ataques y facilitando el manejo de datos ingresados por los usuarios. Es especialmente útil cuando necesitas implementar formularios en tus proyectos web con Flask.

 * Integración con Flask: Flask-WTF está diseñado para funcionar de manera integrada con Flask. Puedes extender tu aplicación Flask y aprovechar las funcionalidades de Flask-WTF para manejar formularios de manera más eficiente.
 * Integración con WTForms: WTForms es una biblioteca de Python que proporciona una forma sencilla de definir y validar formularios. Flask-WTF se encarga de integrar WTForms con Flask, permitiéndote crear formularios con campos, widgets y validadores de manera fácil y organizada.
 * Protección contra ataques CSRF: Cross-Site Request Forgery (CSRF) es un tipo de ataque en el que un sitio malicioso realiza peticiones en nombre del usuario en un sitio legítimo. Flask-WTF incluye mecanismos para proteger tus formularios contra este tipo de ataques mediante el uso de tokens CSRF.
 * Validación de datos: Puedes definir reglas de validación para los campos del formulario utilizando los validadores proporcionados por WTForms. Esto te permite asegurar que los datos ingresados por los usuarios sean válidos antes de procesarlos en el servidor.
 * Renderizado de formularios: Flask-WTF facilita el proceso de renderizado de formularios en plantillas HTML. Puedes generar automáticamente el código HTML necesario para mostrar los formularios en tu sitio web.
 * Procesamiento de datos enviados por formularios: Flask-WTF se encarga de manejar los datos enviados por los usuarios a través de formularios y proporciona métodos para acceder a esos datos en el servidor.
 ## Modulos para realizar conexion con mysql
 > pip install mysqlclient flask-mysql flask-mysqldb
