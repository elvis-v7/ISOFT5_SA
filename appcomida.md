# ADR 1: eleccion de requisitos y tecnologia para app movil

## Contexto  
- **Presupuesto total**: $50,000 MXN que incluye desarrollo, comida para el equipo y gastos operativos. 
   
- **Requisitos clave**:  
  - Nombre: Pikpollo
  - Registro para 500 usuarios.  
  - Sistema de pedidos (solicitar y realizar).  
  - Menú con 3 productos.  
- **Plataforma**: Aplicación móvil para iOS y Android.  

### Frontend (App Móvil)  
- **React Native** ya que lo hemos usado anteriormente en el desarrollo de otra plicacion y tambien se puede usar con python. 

## Infraestructura  
- **Hosting**:  
  - Backend: Render.com o AWS Free Tier (para Python + PostgreSQL).  
  - Base de datos: PostgreSQL en ElephantSQL (plan gratis hasta 20 MB).  
- **Almacenamiento**: Firebase Storage (para imágenes del menú, gratis hasta 1 GB).

## Presupuesto Estimado
- **Comida para equipo (5 personas)**: $1,000 MXN/semana x 4 semanas = $4,000 MXN.  
- **Dominio y hosting**: $1,500 MXN (ejemplo: quickbite.com.mx).  
- **Desarrollo**: $0 (herramientas gratis + trabajo interno).  
- **Marketing**: $5,000 MXN (redes sociales y promociones).  
- **Contingencia**: $7,500 MXN.  
**Total**: el resto puede usarse para escalar o imprevistos.  

# Menú de 3 Productos  
1. **Pollo asado 1/2 o 1/u** - $80 MXN y $160.  
2. **Ensalada de pollo** - $70 MXN.  
3. **pure de papa** - $60 MXN.  

## Flujo de la App  
1. **Registro**: Email + contraseña (autenticación con JWT en Python).  
2. **Pedidos**:  
   - Usuario selecciona productos.  
   - Confirma dirección (guardada en PostgreSQL).  
   - Pago simulado ("efectivo al entregar").  
3. **Admin**: Vista para gestionar pedidos (desde la DB).  

## Status ##
revision pendiente