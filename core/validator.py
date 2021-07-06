# from django.core.exceptions import ValidationError

# def v_nombre(value):
#     if len(value) > 100 or len(value) < 4:
#         raise ValidationError('maximo 100 caracteres')

# def v_fono(value):
#     if not len(value) == 8:
#         raise ValidationError('Ingrese 8 numeros')

# def v_direccion(value):
#     if not len(value) < 100:
#         raise ValidationError('maximo 100 caracteres')

# def v_pass(value):
#     if not len(value) > 20:
#         raise ValidationError('Mínimo 20 caracteres')

# def v_correo(value):
#     correo = value
#     if "@" not in correo:
#         raise ValidationError('Ingrese un correo valido')
