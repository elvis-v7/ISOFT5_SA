# Implementación de Patrón Singleton para Gestión de Estado Global

## Status
Implementado

## Context
El sistema de pollería PickPollo requiere:
    -Gestión consistente del estado de la aplicación entre CLI y API
    -Persistencia de datos en memoria durante la ejecución
    -Acceso controlado a recursos compartidos (usuarios, productos, pedidos)
    -Prevención de múltiples instancias del estado de la aplicación

## Decision
Implementar el patrón Singleton mediante la clase AppStateSingleton que:
    -Garantiza una única instancia del estado de la aplicación
    -Centraliza las operaciones de gestión de datos
    -Proporciona interfaz consistente para CLI y API REST

## Beneficios Obtenidos
    -Estado único: Misma instancia en toda la aplicación
    -Persistencia: Datos mantenidos durante ejecución
    -Consistencia: Mismos datos en CLI y API
    -Encapsulación: Operaciones controladas via métodos
    -Extensibilidad: Fácil agregar nuevas funcionalidades

## Consequences
Positive:
    Estado consistente entre componentes
    Prevención de data races
    Código más organizado y mantenible
    Fácil testing y debugging

## Considerations
    Singleton mantiene estado en memoria (volátil)
    No persistente entre reinicios de aplicación
    Requiere sincronización en entornos multi-hilo