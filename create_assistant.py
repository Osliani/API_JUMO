from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("API_KEY"))

prompt = """
Se te enviarán conversaciones entre un cliente potencial y un asistente virtual. Necesito que extraigas la información de cada uno de los productos y servicios sugeridos por el asistente y la envíes en tu respuesta. En el caso de que se solicite un servicio a pagar por horas el campo product_uom_qty contendrá la cantidad de horas solicitadas por el usuario, en caso contrario será 1 su valor. A continuación el listado de los productos de la empresa con su información detallada: \n [{'product_id': 577, 'name': 'Addon a medida', 'price_unit': 50.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 865, 'name': 'ADDON MuK RES
T API', 'price_unit': 35.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 832, 'name': 'Addon Odoo', 'price_unit': 0.0, 'product_uom': 1, 't
ax_id': [], 'discount': 0.0}, {'product_id': 701, 'name': 'Addon para adjuntar ficheros (copia)', 'price_unit': 75.0, 'product_uom': 1, 'tax_id': [2], 'discount
': 0.0}, {'product_id': 690, 'name': 'Addon para administrar albaranes (copia)', 'price_unit': 100.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'produ
ct_id': 698, 'name': 'Addon para cambiar el tema del backend (copia)', 'price_unit': 84.12, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 69
6, 'name': 'Addon para conectar WooCommerce y Odoo (copia)', 'price_unit': 20.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 680, 'name':
'Addon para diagramas Gantt (copia)', 'price_unit': 40.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 683, 'name': 'Addon para facturar mú
tliples pedidos (copia)', 'price_unit': 100.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 697, 'name': 'Addon para facturar mútliples ped
idos (copia)', 'price_unit': 119.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 705, 'name': 'Addon para generar pedidos desde Intranet (c
opia)', 'price_unit': 200.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 686, 'name': 'Addon para generar pedidos desde Intranet (copia)',
 'price_unit': 100.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 688, 'name': 'Addon para generar reportes financieros (copia)', 'price_u
nit': 400.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 579, 'name': 'Addon para gestión de transporte', 'price_unit': 100.0, 'product_uo
m': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 672, 'name': 'Addon para gestión de transporte (copia)', 'price_unit': 20.0, 'product_uom': 1, 'tax_id':
[2], 'discount': 0.0}, {'product_id': 684, 'name': 'Addon para gestión de transporte (copia)', 'price_unit': 100.0, 'product_uom': 1, 'tax_id': [2], 'discount':
 0.0}, {'product_id': 682, 'name': 'Addon para imágenes (copia)', 'price_unit': 40.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 718, 'na
me': 'Addon Prestashop', 'price_unit': 499.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 582, 'name': 'Algoritmo del modelo', 'price_unit
': 100.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product_id': 675, 'name': 'Alojamiento mensual ERP', 'price_unit': 30.0, 'product_uom': 1, 'tax_i
d': [2], 'discount': 0.0}, {'product_id': 988, 'name': 'Análisis y consultoría', 'price_unit': 80.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'produc
t_id': 585, 'name': 'Análisis y tratamiento de datos', 'price_unit': 100.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product_id': 730, 'name': 'Base
 de datos', 'price_unit': 50.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 839, 'name': 'Billete', 'price_unit': 35.0, 'product_uom': 1,
'tax_id': [], 'discount': 0.0}, {'product_id': 588, 'name': 'Bolsa de horas', 'price_unit': 80.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product_i
d': 689, 'name': 'Comisiones partnership', 'price_unit': 0.0, 'product_uom': 1, 'tax_id': [19], 'discount': 0.0}, {'product_id': 1012, 'name': 'Communication',
'price_unit': 35.0, 'product_uom': 9, 'tax_id': [2], 'discount': 0.0}, {'product_id': 590, 'name': 'Configuración de servidor', 'price_unit': 100.0, 'product_uo
m': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 837, 'name': 'Creación MockUp', 'price_unit': 80.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'
product_id': 838, 'name': 'Creación Web', 'price_unit': 0.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 943, 'name': 'Curso CRM y Ventas'
, 'price_unit': 200.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 591, 'name': 'Desarrollo API', 'price_unit': 80.0, 'product_uom': 1, 't
ax_id': [2], 'discount': 0.0}, {'product_id': 1053, 'name': 'Desarrollo aplicación móvil', 'price_unit': 80.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}
, {'product_id': 595, 'name': 'Desarrollo Back-end', 'price_unit': 80.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 1062, 'name': 'Desarr
ollo Chat Bot', 'price_unit': 80.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product_id': 596, 'name': 'Desarrollo ChatBot', 'price_unit': 80.0, 'pr
oduct_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 597, 'name': 'Desarrollo Ecommerce', 'price_unit': 80.0, 'product_uom': 1, 'tax_id': [2], 'discou
nt': 0.0}, {'product_id': 598, 'name': 'Desarrollo Front-end', 'price_unit': 50.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 599, 'name'
: 'Desarrollo FrontEnd Angular', 'price_unit': 75.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 601, 'name': 'Desarrollo FrontEnd Vue', '
price_unit': 75.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 602, 'name': 'Desarrollo FullStack', 'price_unit': 75.0, 'product_uom': 1,
'tax_id': [2], 'discount': 0.0}, {'product_id': 605, 'name': 'Desarrollo Odoo', 'price_unit': 80.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product
_id': 987, 'name': 'Dietas', 'price_unit': 80.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 733, 'name': 'Diseño gráfico', 'price_unit':
80.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 979, 'name': 'Documentación', 'price_unit': 80.0, 'product_uom': 6, 'tax_id': [2], 'disc
ount': 0.0}, {'product_id': 608, 'name': 'Dominio', 'price_unit': 50.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 609, 'name': 'Down pay
ment', 'price_unit': 1.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 847, 'name': 'Down payment', 'price_unit': 35.0, 'product_uom': 1, '
tax_id': [2], 'discount': 0.0}, {'product_id': 1055, 'name': 'DUA VAT Valuation 10%', 'price_unit': 35.0, 'product_uom': 1, 'tax_id': [193, 2], 'discount': 0.0}
, {'product_id': 1054, 'name': 'DUA VAT Valuation 21%', 'price_unit': 35.0, 'product_uom': 1, 'tax_id': [193, 2], 'discount': 0.0}, {'product_id': 1056, 'name':
 'DUA VAT Valuation 4%', 'price_unit': 35.0, 'product_uom': 1, 'tax_id': [193, 2], 'discount': 0.0}, {'product_id': 614, 'name': 'Entrenamiento del modelo', 'pr
ice_unit': 50.0, 'product_uom': 6, 'tax_id': [], 'discount': 0.0}, {'product_id': 876, 'name': 'Event Registration', 'price_unit': 30.0, 'product_uom': 1, 'tax_
id': [2], 'discount': 0.0}, {'product_id': 836, 'name': 'Expenses', 'price_unit': 0.0, 'product_uom': 1, 'tax_id': [], 'discount': 0.0}, {'product_id': 1069, 'n
ame': 'Fabrica IA', 'price_unit': 10000.0, 'product_uom': 1, 'tax_id': [1, 193], 'discount': 0.0}, {'product_id': 615, 'name': 'Flutter', 'price_unit': 50.0, 'p
roduct_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product_id': 616, 'name': 'Flutter App', 'price_unit': 3500.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0
.0}, {'product_id': 617, 'name': 'Formación Odoo', 'price_unit': 80.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product_id': 954, 'name': 'Gastos fi
nancieros', 'price_unit': 35.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 734, 'name': 'Gastos financieros SEPA', 'price_unit': 0.0, 'pr
oduct_uom': 1, 'tax_id': [33], 'discount': 0.0}, {'product_id': 844, 'name': 'Gestión contable y laboral', 'price_unit': 0.0, 'product_uom': 1, 'tax_id': [2], '
discount': 0.0}, {'product_id': 1015, 'name': 'Gifts', 'price_unit': 35.0, 'product_uom': 9, 'tax_id': [2], 'discount': 0.0}, {'product_id': 840, 'name': 'Hardw
are', 'price_unit': 0.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 619, 'name': 'Hosting', 'price_unit': 100.0, 'product_uom': 1, 'tax_i
d': [2], 'discount': 0.0}, {'product_id': 1065, 'name': 'IA Madre', 'price_unit': 10000.0, 'product_uom': 1, 'tax_id': [1, 193], 'discount': 0.0}, {'product_id'
: 622, 'name': 'Implantación Odoo', 'price_unit': 2500.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 623, 'name': 'Implantación Prestasho
p', 'price_unit': 800.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 626, 'name': 'Implementación del algoritmo', 'price_unit': 35.0, 'pro
duct_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 627, 'name': 'Implementación del modelo', 'price_unit': 50.0, 'product_uom': 1, 'tax_id': [2], 'di
scount': 0.0}, {'product_id': 624, 'name': 'Implementación Firebase', 'price_unit': 65.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 729,
 'name': 'Instalación Addon', 'price_unit': 80.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product_id': 629, 'name': 'Integración', 'price_unit': 75
.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 630, 'name': 'Integración Api', 'price_unit': 80.0, 'product_uom': 1, 'tax_id': [2], 'disc
ount': 0.0}, {'product_id': 934, 'name': 'Inteligencia Artificial', 'price_unit': 80.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product_id': 951, '
name': 'Licencia', 'price_unit': 1200.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 1061, 'name': 'Licencias Odoo Community Plus', 'price
_unit': 0.0, 'product_uom': 1, 'tax_id': [193, 2], 'discount': 0.0}, {'product_id': 950, 'name': 'Licencias RingOver', 'price_unit': 40.0, 'product_uom': 1, 'ta
x_id': [2], 'discount': 0.0}, {'product_id': 704, 'name': 'Mantenimiento', 'price_unit': 150.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id'
: 1014, 'name': 'Meals', 'price_unit': 35.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 636, 'name': 'Migración', 'price_unit': 80.0, 'pr
oduct_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product_id': 1010, 'name': 'Mileage', 'price_unit': 35.0, 'product_uom': 9, 'tax_id': [2], 'discount': 0.0}, {
'product_id': 1018, 'name': 'Miravia', 'price_unit': 1800.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 678, 'name': 'MNMRKT', 'price_uni
t': 380.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 637, 'name': 'MockUp', 'price_unit': 80.0, 'product_uom': 6, 'tax_id': [2], 'discou
nt': 0.0}, {'product_id': 731, 'name': 'Módulo BC3', 'price_unit': 500.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 638, 'name': 'Odoo',
 'price_unit': 80.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product_id': 676, 'name': 'Odoo Asistencia Técnica', 'price_unit': 65.0, 'product_uom'
: 6, 'tax_id': [2], 'discount': 0.0}, {'product_id': 932, 'name': 'Odoo mirakl connector', 'price_unit': 2000.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.
0}, {'product_id': 1052, 'name': 'Odoo SAS', 'price_unit': 0.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 687, 'name': 'Odoo SEO', 'pric
e_unit': 50.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 1013, 'name': 'Others', 'price_unit': 35.0, 'product_uom': 1, 'tax_id': [2], 'd
iscount': 0.0}, {'product_id': 933, 'name': 'Pack de horas generales', 'price_unit': 1600.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product_id': 6
42, 'name': 'Plugin', 'price_unit': 100.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 841, 'name': 'portes', 'price_unit': 35.0, 'product
_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 643, 'name': 'Predicción del modelo', 'price_unit': 50.0, 'product_uom': 1, 'tax_id': [2], 'discount':
 0.0}, {'product_id': 842, 'name': 'Productos de limpieza', 'price_unit': 0.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 645, 'name': 'R
ecopilación de datos', 'price_unit': 100.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product_id': 646, 'name': 'Resolución de bugs', 'price_unit': 3
5.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 647, 'name': 'Restyling', 'price_unit': 35.0, 'product_uom': 1, 'tax_id': [2], 'discount'
: 0.0}, {'product_id': 868, 'name': 'Seguros', 'price_unit': 192.73, 'product_uom': 1, 'tax_id': [33], 'discount': 0.0}, {'product_id': 650, 'name': 'SEO', 'pri
ce_unit': 50.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 721, 'name': 'SEO', 'price_unit': 65.0, 'product_uom': 6, 'tax_id': [2], 'disc
ount': 0.0}, {'product_id': 722, 'name': 'SEO (copia)', 'price_unit': 100.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 654, 'name': 'Ser
ialización', 'price_unit': 75.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 834, 'name': 'Service on Timesheet', 'price_unit': 75.0, 'pro
duct_uom': 6, 'tax_id': [], 'discount': 0.0}, {'product_id': 845, 'name': 'Servicio de alarma', 'price_unit': 1.0, 'product_uom': 1, 'tax_id': [], 'discount': 0
.0}, {'product_id': 1049, 'name': 'Servicio de mensajería', 'price_unit': 35.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 710, 'name': '
Servicio de telefonía', 'price_unit': 0.0, 'product_uom': 1, 'tax_id': [], 'discount': 0.0}, {'product_id': 655, 'name': 'Servicio personalización addons', 'pri
ce_unit': 40.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 863, 'name': 'Servicios Odoo', 'price_unit': 0.0, 'product_uom': 1, 'tax_id':
[], 'discount': 0.0}, {'product_id': 703, 'name': 'Servidor', 'price_unit': 80.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 977, 'name':
 'Servidor Odoo', 'price_unit': 0.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 852, 'name': 'Soporte', 'price_unit': 0.0, 'product_uom':
 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 709, 'name': 'Soporte 360 A', 'price_unit': 3600.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'pro
duct_id': 706, 'name': 'Soporte 360 M', 'price_unit': 0.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 1058, 'name': 'Standard delivery',
'price_unit': 0.0, 'product_uom': 1, 'tax_id': [1, 193], 'discount': 0.0}, {'product_id': 833, 'name': 'Subida Apps Store', 'price_unit': 50.0, 'product_uom': 1
, 'tax_id': [2], 'discount': 0.0}, {'product_id': 666, 'name': 'Testing y Validación', 'price_unit': 80.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'
product_id': 723, 'name': 'Traducción', 'price_unit': 35.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 846, 'name': 'TRANSPORTE', 'price_
unit': 35.0, 'product_uom': 1, 'tax_id': [], 'discount': 0.0}, {'product_id': 1009, 'name': 'Travel & Accommodation', 'price_unit': 35.0, 'product_uom': 1, 'tax
_id': [2], 'discount': 0.0}, {'product_id': 944, 'name': 'Upgrade Odo', 'price_unit': 3500.0, 'product_uom': 6, 'tax_id': [2], 'discount': 0.0}, {'product_id':
1042, 'name': 'Upgrade Odoo Community', 'price_unit': 3500.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 667, 'name': 'Validación del mod
elo', 'price_unit': 50.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}, {'product_id': 843, 'name': 'Varios', 'price_unit': 1.0, 'product_uom': 1, 'tax_id'
: [], 'discount': 0.0}, {'product_id': 1068, 'name': 'Viaticos', 'price_unit': 300.0, 'product_uom': 1, 'tax_id': [193, 2], 'discount': 0.0}, {'product_id': 106
4, 'name': 'Virtual Empowerment', 'price_unit': 500.0, 'product_uom': 1, 'tax_id': [193, 2], 'discount': 0.0}, {'product_id': 668, 'name': 'Web', 'price_unit':
65.0, 'product_uom': 1, 'tax_id': [2], 'discount': 0.0}] \n
Por favor, responde estrictamente en el siguiente formato JSON (para poder convertir los datos en un dicionario python con json.loads() al recibirlos):
[
  {
    "product_name": "string",
    "product_id": number,
    "price_unit": number,
    "product_uom": number,
    "discount": number,
    "product_uom_qty": number
  }
]
Ejemplo:
[
  {
    "product_name": "Bolsa de horas",
    "product_id": 478,
    "price_unit": 80,
    "product_uom": 6,
    "discount": 0,
    "product_uom_qty": 40
  }
]
Los parametros que no se encuentren enviarlos como "Empty" si es string o como -1 si es number. Recuerda solo extraer los productos recomendados por el asistente.
"""

assistant = client.beta.assistants.create (
  name = "Extractor_16",
  instructions = prompt,
  model = "gpt-4-1106-preview",
)

print(assistant.id)