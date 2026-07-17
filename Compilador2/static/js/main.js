const formulario = document.getElementById("analyzeForm");
const entradaArchivo = document.getElementById("sourcefile");
const textoEtiquetaArchivo = document.getElementById("fileLabelText");
const zonaArrastre = document.getElementById("fileDrop");
const botonAnalizar = document.getElementById("analyzeBtn");

const tarjetaProgreso = document.getElementById("progressCard");
const rellenoProgreso = document.getElementById("progressFill");
const estadoProgreso = document.getElementById("progressStatus");
const pasosFase = document.getElementById("phaseSteps");

const tarjetaResultados = document.getElementById("resultsCard");
const contenidoResultados = document.getElementById("resultsContent");

const ORDEN_FASES = ["upload", "lexico", "sintactico", "semantico"];
const PORCENTAJE_OBJETIVO_FASE = { upload: 25, lexico: 50, sintactico: 75, semantico: 95 };

// -------------------- Nombre de archivo seleccionado --------------------
entradaArchivo.addEventListener("change", () => {
    if (entradaArchivo.files.length > 0) {
        textoEtiquetaArchivo.textContent = entradaArchivo.files[0].name;
    } else {
        textoEtiquetaArchivo.textContent = "Selecciona un archivo o arrástralo aquí";
    }
});

["dragover", "dragleave", "drop"].forEach((evento) => {
    zonaArrastre.addEventListener(evento, (e) => {
        e.preventDefault();
        zonaArrastre.classList.toggle("drag-over", evento === "dragover");
    });
});
zonaArrastre.addEventListener("drop", (e) => {
    if (e.dataTransfer.files.length > 0) {
        entradaArchivo.files = e.dataTransfer.files;
        textoEtiquetaArchivo.textContent = e.dataTransfer.files[0].name;
    }
});

// ------------------------------ Envio -----------------------------------
formulario.addEventListener("submit", async (e) => {
    e.preventDefault();

    if (!entradaArchivo.files.length) return;

    reiniciarInterfazProgreso();
    tarjetaResultados.hidden = true;
    tarjetaProgreso.hidden = false;
    botonAnalizar.disabled = true;

    const datosFormulario = new FormData();
    datosFormulario.append("archivo_fuente", entradaArchivo.files[0]);
    establecerFase("upload", "active");
    establecerProgreso(10, "Subiendo archivo al servidor…");

    const temporizadorSimulacion = simularProgresoIntermedio();

    try {
        const respuesta = await fetch("/api/analyze", {
            method: "POST",
            body: datosFormulario,
        });

        clearInterval(temporizadorSimulacion);

        const datos = await respuesta.json();

        if (!respuesta.ok && datos.error_servidor) {
            establecerProgreso(100, "Error antes de iniciar el análisis.");
            marcarTodasFasesDesconocidas();
            renderizarErrorServidor(datos.error_servidor);
            return;
        }

        renderizarResultado(datos);
    } catch (err) {
        clearInterval(temporizadorSimulacion);
        establecerProgreso(100, "Error de comunicación con el servidor.");
        marcarTodasFasesDesconocidas();
        renderizarErrorServidor("No fue posible contactar al servidor: " + err.message);
    } finally {
        botonAnalizar.disabled = false;
    }
});

function simularProgresoIntermedio() {
    let paso = 0;
    const secuencia = ["upload", "lexico", "sintactico"];
    return setInterval(() => {
        if (paso >= secuencia.length) return;
        const fase = secuencia[paso];
        establecerFase(fase, "active");
        establecerProgreso(PORCENTAJE_OBJETIVO_FASE[fase], etiquetaFase(fase) + "…");
        paso += 1;
    }, 450);
}

// --------------------------- Render del resultado ------------------------
function renderizarResultado(datos) {
    if (datos.exito) {
        establecerProgreso(100, "Análisis completado con éxito.");
        ORDEN_FASES.forEach((f) => establecerFase(f, "done"));
        renderizarExito(datos);
    } else {
        const faseDetenida = datos.fase_detenida || "semantico";
        marcarFasesHasta(faseDetenida);
        establecerProgreso(100, "Análisis detenido en: " + (datos.fase_detenida_etiqueta || faseDetenida));
        renderizarErrores(datos);
    }
}

function renderizarExito(datos) {
    tarjetaResultados.hidden = false;
    let html = `<div class="result-banner success">✔ El código no presenta errores léxicos, sintácticos ni semánticos.</div>`;

    html += `<div class="stats-grid">
        <div class="stat-box"><div class="stat-value">${datos.conteo_tokens}</div><div class="stat-label">Tokens generados</div></div>
        <div class="stat-box"><div class="stat-value">${datos.conteo_reglas}</div><div class="stat-label">Nodos de regla (parser)</div></div>
    </div>`;

    if (datos.tabla_tokens && datos.tabla_tokens.length) {
        html += `<p style="margin-top:1rem;"><strong>Tabla de tokens:</strong></p>
                  <div class="token-table-wrap">
                    <table class="token-table">
                        <thead><tr><th>Token</th><th>Lexema</th></tr></thead>
                        <tbody>` +
            datos.tabla_tokens.map(t => `<tr><td>${escaparHtml(t.token)}</td><td>${escaparHtml(t.lexema)}</td></tr>`).join("") +
            `</tbody>
                    </table>
                  </div>`;
    }
    if (datos.vista_previa_arbol) {
        html += `<p style="margin-top:1rem;"><strong>Árbol sintáctico (vista previa):</strong></p>
                  <div class="tree-preview">${escaparHtml(datos.vista_previa_arbol)}</div>`;
    }

    contenidoResultados.innerHTML = html;
}

function renderizarErrores(datos) {
    tarjetaResultados.hidden = false;
    const etiquetaFaseActual = datos.fase_detenida_etiqueta || "desconocida";

    let html = `<div class="result-banner error">✘ El análisis se detuvo en la fase: ${escaparHtml(etiquetaFaseActual)}.</div>`;
    html += `<ul class="error-list">`;
    datos.errores.forEach((err) => {
        html += `<li class="error-item">
            <span class="location">Línea ${err.linea}, columna ${err.columna} — ${escaparHtml(err.fase_etiqueta)}</span>
            ${escaparHtml(err.mensaje)}
        </li>`;
    });
    html += `</ul>`;

    contenidoResultados.innerHTML = html;
}

function renderizarErrorServidor(mensaje) {
    tarjetaResultados.hidden = false;
    contenidoResultados.innerHTML = `<div class="result-banner error">✘ ${escaparHtml(mensaje)}</div>`;
}

// ------------------------------ Utilidades --------------------------------
function reiniciarInterfazProgreso() {
    establecerProgreso(0, "Esperando…");
    Array.from(pasosFase.children).forEach((li) => {
        li.classList.remove("active", "done", "failed");
    });
}

function establecerProgreso(porcentaje, textoEstado) {
    rellenoProgreso.style.width = porcentaje + "%";
    estadoProgreso.textContent = textoEstado;
}

function establecerFase(claveFase, estado) {
    const li = pasosFase.querySelector(`[data-phase="${claveFase}"]`);
    if (!li) return;
    li.classList.remove("active", "done", "failed");
    li.classList.add(estado);
}

function marcarFasesHasta(faseFallida) {
    const idx = ORDEN_FASES.indexOf(faseFallida);
    ORDEN_FASES.forEach((f, i) => {
        if (i < idx) establecerFase(f, "done");
        else if (i === idx) establecerFase(f, "failed");
    });
}

function marcarTodasFasesDesconocidas() {
    ORDEN_FASES.forEach((f) => establecerFase(f, "failed"));
}

function etiquetaFase(claveFase) {
    const etiquetas = {
        upload: "Subiendo archivo",
        lexico: "Ejecutando análisis léxico",
        sintactico: "Ejecutando análisis sintáctico",
        semantico: "Ejecutando análisis semántico",
    };
    return etiquetas[claveFase] || claveFase;
}

function escaparHtml(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
}
