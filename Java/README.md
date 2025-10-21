# FizzBuzzKata (subproyecto Java)

Este directorio contiene la implementación Java de la FizzBuzz kata, junto con tests y utilidades para ejecutar la aplicación.

Este README explica cómo preparar el entorno, compilar, ejecutar la clase `Main`, ejecutar tests y generar la documentación (Javadoc).

## Requisitos

- JDK 21 (u otra JDK compatible, pero el proyecto está compilado con `--release 21`).
  - Ejemplo de instalación en Windows: Eclipse Adoptium / Temurin.
  - Asegúrate de que `java` y `javac` en la terminal apuntan a la JDK adecuada.
  - Opcional: configura la variable de entorno `JAVA_HOME`.

- Apache Maven (si no usas el Maven Wrapper): versión 3.8.x o superior.

- (Opcional) IDE como IntelliJ IDEA, Eclipse o VS Code para desarrollo.

## Estructura relevante

- `src/main/java` — código fuente (paquete `com.carlos`).
- `src/test/java` — tests JUnit 5.
- `pom.xml` — configuración de Maven para el módulo Java.
- `run.ps1` — script PowerShell para compilar y ejecutar `Main`.
- `run.cmd` — script CMD para compilar y ejecutar `Main`.

> Nota: la mayoría de comandos deben ejecutarse desde este directorio (`Java`) porque contiene el `pom.xml` del subproyecto.

## Comandos útiles (PowerShell)

Abrir PowerShell y navegar al directorio `Java`:

```powershell
cd 'C:\Users\carlo\OneDrive\Escritorio\Prácticas Externas\FizzBuzzKata\Java'
```

### 1) Compilar

Compilar el proyecto (sin ejecutar tests):

```powershell
mvn -DskipTests package
```

O compilar (fase compile):

```powershell
mvn compile
```

### 2) Ejecutar la clase Main

Hay varias opciones; las más sencillas están ya configuradas.

- Usando el plugin `exec` de Maven (configurado en `pom.xml`):

```powershell
mvn exec:java
```

- Usando el script PowerShell (compila si hace falta y ejecuta):

```powershell
.\run.ps1
```

- Usando el script CMD en Windows (desde CMD):

```
run.cmd
```

Si prefieres ejecutar directamente la JVM sobre las clases compiladas:

```powershell
# primero compilar
mvn -DskipTests package
# luego ejecutar
java -cp target/classes com.carlos.Main
```

### 3) Ejecutar tests (JUnit 5)

- Ejecutar todos los tests:

```powershell
mvn test
```

- Ejecutar una clase de test concreta (p. ej. `FizzBuzzTest`):

```powershell
mvn -Dtest=FizzBuzzTest test
```

- Ejecutar un único método de test:

```powershell
mvn -Dtest=FizzBuzzTest#constructorThrowsOnInvalidLimit test
```

### 4) Generar Javadoc

Genera la documentación API en HTML:

```powershell
mvn javadoc:javadoc
```

Salida: `target/site/apidocs/index.html`.

### 5) (Opcional) Usar Maven Wrapper

Si quieres permitir ejecutar Maven sin instalarlo en la máquina, puedes añadir el Maven Wrapper (`mvnw`/`mvnw.cmd`). Para generarlo (localmente):

```powershell
mvn -N io.takari:maven:wrapper
```

Después puede usarse `./mvnw.cmd test` (Windows) o `./mvnw test` (Unix).

## Configuración del JDK (Windows)

- Verifica la versión de Java:

```powershell
java -version
javac -version
```

- Si necesitas apuntar a una JDK concreta (ejemplo):

```powershell
$env:JAVA_HOME = 'C:\Program Files\Eclipse Adoptium\jdk-21.0.8.9-hotspot'
$env:Path = $env:JAVA_HOME + '\bin;' + $env:Path
```

Puedes añadir `JAVA_HOME` permanentemente desde la Configuración de variables de entorno de Windows.