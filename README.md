# Customer Portal
La aplicación se llama Customer Portal, consta de 3 modelos llamados: `Company`, `Client` y `Ticket`.
En esta aplicación puedes crear companías, clientes y tickets para soporte de los clientes. También podrás buscar tus tickets.

## ¿Cómo probar?
- Para empezar debes crear una compañía.
- Luego vas a crear un cliente, este cliente quedará anclado a la compañía.
- Finalmente, pasarás a crear un ticket, este ticket estará asociado al cliente. 
- Puedes buscar tickets usando el email de los clientes.
- Si deseas probar la aplicación como Admin deberás crear un superuser usando el comando `python manage.py createsuperuser`.

Dentro de cada una de las vistas podrás encontrar las relaciones a través de los modelos. Por ejemplo:
    - Desde clientes puedes ir a compañías y viceversa.

## Código
El código está ubicado en la aplicación de Django `customer_portal` usando los archivos `models.py`, `forms.py`, `views.py` y `urls.py`.
También hay una carpeta de `templates` con todos los HTMl necesarios para la página. Adicional, se añadió un pequeño archivo CSS con algunos estilos básicos.
