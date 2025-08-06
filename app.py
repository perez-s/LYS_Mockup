import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime, timedelta
from streamlit_drawable_canvas import st_canvas
import plotly.express as px

# Título de la aplicación

st.set_page_config(page_title="LYS DEMO", layout="wide")
st.image("assets/logo_lys.png", width=500)


st.title("LYS DEMO - HERRAMIENTA DE GESTIÓN DIGITAL")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Modulo de Hoja de ruta",
    "Modulo de Aforos",
    "Modulo de PQR",
    "Modulo de Dasboard",
    "Modulo de Cartera"    
])

################ TAB 1: Hoja de Ruta ##############################

with tab1:

    st.title("📋 Formato Hoja de Ruta")

    st.write("Complete la siguiente información para registrar la hoja de ruta del vehículo de recolección.")

    
    
    with st.form("hoja_ruta_form"):

        col1, col2 = st.columns(2)
    
        with col1:

            # Información general
            fecha = st.date_input("Fecha", value=datetime.today())
            hora = st.time_input("Hora", value=datetime.now().time())
            vehiculo = st.selectbox(
                "Vehículo",
                ["Camión 1", "Camión 2", "Camión 3", "Camión 4", "Camión 5"]
            )
            conductor = st.selectbox(
                "Conductor",
                ["Juan Pérez", "María López", "Carlos García", "Ana Torres", "Luis Martínez"]
            )
            auxiliar = st.selectbox(
                "Auxiliar",
                ["Pedro Sánchez", "Laura Jiménez", "Sofía Ruiz", "Andrés Díaz", "Clara Fernández"]
            )
            ruta = st.selectbox(
                "Ruta",
                ["Ruta Norte", "Ruta Sur", "Ruta Este", "Ruta Oeste", "Ruta Centro"]
            )
        
            # Medidores
            kilometraje_inicial = st.number_input("Kilometraje Inicial", min_value=0, step=1)
        with col2:
            kilometraje_final = st.number_input("Kilometraje Final", min_value=0, step=1)
            horometro_inicial = st.number_input("Horómetro Inicial", min_value=0, step=1)
            horometro_final = st.number_input("Horómetro Final", min_value=0, step=1)
            
            # Recolección
            tipo_residuo = st.selectbox(
                "Tipo de Residuo",
                ["Ordinario", "Reciclable", "Especial", "Hospitalario", "Otros"]
            )
            toneladas_recogidas = st.number_input("Toneladas Recogidas", min_value=0.0, step=0.1)
            numero_viajes = st.number_input("Número de Viajes", min_value=1, step=1)
            
            # Observaciones
            observaciones = st.text_area("Observaciones", placeholder="Anotar novedades de la ruta...")

            # Botón para guardar
        submit_button = st.form_submit_button("Guardar Registro")

    # Al enviar el formulario
    if submit_button:
        datos = {
            "Fecha": [fecha],
            "Hora": [hora.strftime("%H:%M")],
            "Vehículo": [vehiculo],
            "Conductor": [conductor],
            "Auxiliar": [auxiliar],
            "Ruta": [ruta],
            "Km Inicial": [kilometraje_inicial],
            "Km Final": [kilometraje_final],
            "Horómetro Inicial": [horometro_inicial],
            "Horómetro Final": [horometro_final],
            "Tipo de Residuo": [tipo_residuo],
            "Toneladas": [toneladas_recogidas],
            "Viajes": [numero_viajes],
            "Observaciones": [observaciones],
        }

        df = pd.DataFrame(datos)
        st.success("✅ Registro guardado correctamente.")
        st.dataframe(df)

        # Opcional: guardar en CSV
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="⬇️ Descargar en CSV",
            data=csv,
            file_name=f"hoja_ruta_{fecha}.csv",
            mime="text/csv",
        )
################ TAB 2: Aforos ##############################

with tab2:

    st.title("📑 Formato de Aforo")

    with st.form("form_aforo"):
        # Crear dos columnas
        col1, col2 = st.columns(2)

        with col1:
            fecha = st.date_input("Fecha", value=datetime.today())
            hora = st.time_input("Hora", value=datetime.now().time())
            consecutivo = st.text_input("Consecutivo")
            clase_servicio = st.selectbox("Clase de Servicio", ["Ordinario", "Reciclable", "Especial", "Otros"])
            codigo_vehiculo = st.text_input("Código del Vehículo")
            zona_prestacion = st.selectbox("Zona de Prestación", ["Zona 1", "Zona 2", "Zona 3", "Zona 4"])
            cuenta_contrato = st.text_input("Cuenta Contrato")
            nombre_usuario = st.selectbox(
                "Nombre del Usuario",
                ["Usuario 1", "Usuario 2", "Usuario 3", "Usuario 4", "Usuario 5"]
            )
            direccion = st.text_input("Dirección de Servicio / Usuario")
            correo = st.text_input("Correo Electrónico")
            barrio = st.text_input("Barrio")

        with col2:
            factura = st.text_input("Factura")
            placa = st.text_input("Placa del Vehículo")
            cedula_nit = st.text_input("Cédula / NIT")
            comuna = st.text_input("Comuna")
            telefono = st.text_input("Teléfono")
            observaciones = st.text_area("Observaciones")
            ejecutado_por = st.selectbox(
                "Ejecutado por",
                ["Operador 1", "Operador 2", "Operador 3", "Operador 4", "Operador 5"]
            )
            # Aceptación del usuario
            aceptacion_usuario = st.text_input("Aceptación Usuario (nombre cliente)")
            tipo_observacion = st.text_input("Tipo de Observación")
            autorizacion_cargue = st.selectbox("Autorización Cargue Sistema Comercial", ["Sí", "No"])
            evidencia_fotografica = st.camera_input("📸 Evidencia Fotográfica")

        # Labores realizadas (tabla editable)
        st.subheader("🛠️ Labores Realizadas")
        items = st.text_area(
            "Ingrese los ítems en formato: Descripción, Cantidad, Cálculo m³ (una línea por ítem)",
            "Contenedores 1100 LTS, 1, 1.1\nContenedores 800 LTS, 1, 0.8"
        )

        col3, col4 = st.columns(2)
        with col3:
            st.write("Firma 1")
            canvas_result = st_canvas(
                stroke_width=1,
                stroke_color= "#000000",
                background_color="#7a7474",
                height=150,
                key="canvas",
                update_streamlit=True
            )      
        with col4:
            st.write("Firma 2")
            canvas_result = st_canvas(
                stroke_width=1,
                stroke_color= "#000000",
                background_color="#7a7474",
                height=150,
                key="canvas2",
                update_streamlit=True
            )   
        # Botón
        submit = st.form_submit_button("Guardar Aforo")
         
    if submit:
        # Procesar tabla de labores
        labores = []
        for linea in items.splitlines():
            partes = [p.strip() for p in linea.split(",")]
            if len(partes) == 3:
                labores.append({"Descripción": partes[0], "Cantidad": partes[1], "Cálculo m³": partes[2]})

        df_labores = pd.DataFrame(labores)

        # Mostrar resumen
        st.success("✅ Aforo registrado correctamente")

        st.write("### Resumen de Datos")
        st.json({
            "Fecha": str(fecha),
            "Hora": hora.strftime("%H:%M"),
            "Consecutivo": consecutivo,
            "Factura": factura,
            "Clase de Servicio": clase_servicio,
            "Código Vehículo": codigo_vehiculo,
            "Placa": placa,
            "Zona de Prestación": zona_prestacion,
            "Cuenta Contrato": cuenta_contrato,
            "Cédula / NIT": cedula_nit,
            "Usuario": nombre_usuario,
            "Dirección": direccion,
            "Correo": correo,
            "Barrio": barrio,
            "Comuna": comuna,
            "Teléfono": telefono,
            "Tipo Observación": tipo_observacion,
            "Observaciones": observaciones,
            "Autorización Cargue": autorizacion_cargue,
            "Ejecutado por": ejecutado_por,
            "Aceptación Usuario": aceptacion_usuario
        })

        st.write("### Labores Realizadas")
        st.table(df_labores)

        # Guardar CSV
        csv = df_labores.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Descargar Labores en CSV",
            csv,
            file_name=f"labores_aforo_{fecha}.csv",
            mime="text/csv"
        )
################ TAB 3: PQR ##############################
with tab3:

    st.title("📌 Gestión de PQRs con Calendario de Vencimientos")

    # ----------------------------
    # Datos iniciales de muestra
    # ----------------------------
    pqr_data = [
        {"ID": 1, "Tipo": "Petición", "Usuario": "Carlos Pérez", "Descripción": "Solicitud de cambio de contenedor", 
        "Fecha Radicación": datetime(2025, 8, 1), "Fecha Vencimiento": datetime(2025, 8, 16), "Estado": "Pendiente"},
        {"ID": 2, "Tipo": "Queja", "Usuario": "María Gómez", "Descripción": "Retraso en recolección de residuos", 
        "Fecha Radicación": datetime(2025, 8, 3), "Fecha Vencimiento": datetime(2025, 8, 18), "Estado": "En proceso"},
        {"ID": 3, "Tipo": "Reclamo", "Usuario": "Juan López", "Descripción": "Cobro indebido en factura", 
        "Fecha Radicación": datetime(2025, 7, 29), "Fecha Vencimiento": datetime(2025, 8, 13), "Estado": "Pendiente"},
    ]

    df_pqrs = pd.DataFrame(pqr_data)

    # ----------------------------
    # Formulario para ingresar PQR
    # ----------------------------
    st.subheader("✍️ Ingresar nueva PQR")

    with st.form("form_pqr"):
        col1, col2 = st.columns(2)
        with col1:
            tipo = st.selectbox("Tipo de PQR", ["Petición", "Queja", "Reclamo"])
            usuario = st.text_input("Nombre del Usuario")
            descripcion = st.text_area("Descripción del caso")
        with col2:
            fecha_radicacion = st.date_input("Fecha de Radicación", value=datetime.today())
            dias_vencimiento = st.number_input("Plazo de Respuesta (días)", value=15, min_value=1)
            estado = st.selectbox("Estado", ["Pendiente", "En proceso", "Cerrado"])

        submit = st.form_submit_button("Guardar PQR")

    if submit:
        nuevo_id = df_pqrs["ID"].max() + 1 if not df_pqrs.empty else 1
        
        # Convertir fecha_radicacion (date) a datetime
        fecha_radicacion_dt = datetime.combine(fecha_radicacion, datetime.min.time())
        fecha_vencimiento = fecha_radicacion_dt + timedelta(days=dias_vencimiento)
        
        nueva_pqr = {
            "ID": nuevo_id,
            "Tipo": tipo,
            "Usuario": usuario,
            "Descripción": descripcion,
            "Fecha Radicación": fecha_radicacion_dt,
            "Fecha Vencimiento": fecha_vencimiento,
            "Estado": estado,
        }
        
        df_pqrs = pd.concat([df_pqrs, pd.DataFrame([nueva_pqr])], ignore_index=True)
        
        # 🔑 Asegurar tipos de fecha correctos
        df_pqrs["Fecha Radicación"] = pd.to_datetime(df_pqrs["Fecha Radicación"])
        df_pqrs["Fecha Vencimiento"] = pd.to_datetime(df_pqrs["Fecha Vencimiento"])

        st.success(f"✅ PQR registrada con ID {nuevo_id}")

    # ----------------------------
    # Tabla de PQRs
    # ----------------------------
    st.subheader("📋 Listado de PQRs")
    st.dataframe(df_pqrs, use_container_width=True)

    # ----------------------------
    # Calendario de vencimientos
    # ----------------------------
    st.subheader("📅 Calendario de Vencimientos")

    df_cal = df_pqrs.copy()
    df_cal["Fecha Radicación"] = pd.to_datetime(df_cal["Fecha Radicación"])
    df_cal["Fecha Vencimiento"] = pd.to_datetime(df_cal["Fecha Vencimiento"])

    fig = px.timeline(
        df_cal,
        x_start="Fecha Radicación",
        x_end="Fecha Vencimiento",
        y="Usuario",
        color="Tipo",
        text="Estado",
        title="PQRs y sus fechas de vencimiento"
    )

    fig.update_yaxes(autorange="reversed")  # para que se vea como calendario
    st.plotly_chart(fig, use_container_width=True)

    # ----------------------------
    # Mostrar próximo vencimiento
    # ----------------------------
    st.subheader("⏳ Próximo Vencimiento")

    hoy = datetime.today()
    df_pendientes = df_cal[df_cal["Estado"] != "Cerrado"]
    df_pendientes["Días Restantes"] = (df_pendientes["Fecha Vencimiento"] - hoy).dt.days

    if not df_pendientes.empty:
        prox = df_pendientes.sort_values("Fecha Vencimiento").iloc[0]
        st.warning(
            f"⚠️ La PQR con ID **{prox['ID']}** del usuario **{prox['Usuario']}** "
            f"vence el **{prox['Fecha Vencimiento'].strftime('%Y-%m-%d')}** "
            f"({prox['Días Restantes']} días restantes)."
        )
    else:
        st.info("✅ No hay PQRs pendientes por vencer.")

################ TAB 4: Dashboard ##############################

with tab4:



    st.title("📊 Dashboard Integral - Empresa de Aseo")

    # ==========================
    # Datos de Muestra
    # ==========================
    # Hoja de Ruta
    hojas_ruta = pd.DataFrame([
        {"Fecha": "2025-08-01", "Vehículo": "ABC123", "Ruta": "Norte", "Toneladas": 5.2},
        {"Fecha": "2025-08-01", "Vehículo": "XYZ987", "Ruta": "Sur", "Toneladas": 6.8},
        {"Fecha": "2025-08-02", "Vehículo": "ABC123", "Ruta": "Centro", "Toneladas": 4.5},
    ])

    # Aforos
    aforos = pd.DataFrame([
        {"Consecutivo": "AF-001", "Usuario": "Conjunto Los Álamos", "m3": 1.1},
        {"Consecutivo": "AF-002", "Usuario": "Colegio Distrital", "m3": 0.8},
        {"Consecutivo": "AF-003", "Usuario": "Hospital Central", "m3": 2.5},
    ])

    # PQRs
    pqrs = pd.DataFrame([
        {"ID": 1, "Tipo": "Petición", "Usuario": "Carlos Pérez", "Fecha Vencimiento": datetime(2025,8,16), "Estado": "Pendiente"},
        {"ID": 2, "Tipo": "Queja", "Usuario": "María Gómez", "Fecha Vencimiento": datetime(2025,8,18), "Estado": "En proceso"},
        {"ID": 3, "Tipo": "Reclamo", "Usuario": "Juan López", "Fecha Vencimiento": datetime(2025,8,13), "Estado": "Pendiente"},
    ])

    # Cartera
    cartera = pd.DataFrame([
        {"Cliente": "Carlos Pérez", "Saldo": 1200000, "Estado": "Mora"},
        {"Cliente": "María Gómez", "Saldo": 0, "Estado": "Corriente"},
        {"Cliente": "Juan López", "Saldo": 350000, "Estado": "Mora"},
        {"Cliente": "Empresa XYZ", "Saldo": 2000000, "Estado": "Mora"},
    ])

    # ==========================
    # KPIs principales
    # ==========================
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🚛 Rutas realizadas", hojas_ruta.shape[0])
    with col2:
        st.metric("♻️ Toneladas recogidas", f"{hojas_ruta['Toneladas'].sum():.1f}")
    with col3:
        st.metric("📑 Aforos generados", aforos.shape[0])
    with col4:
        st.metric("📌 PQRs pendientes", pqrs[pqrs['Estado']!='Cerrado'].shape[0])

    # ==========================
    # Visualizaciones en columnas
    # ==========================
    colA, colB = st.columns(2)

    with colA:
        st.subheader("🚛 Toneladas Recogidas por Ruta")
        fig1 = px.bar(hojas_ruta, x="Ruta", y="Toneladas", color="Vehículo", title="Producción de residuos")
        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("📑 Aforos por Usuario")
        fig2 = px.pie(aforos, values="m3", names="Usuario", title="Distribución de m³ aforados")
        st.plotly_chart(fig2, use_container_width=True)

    with colB:
        st.subheader("📌 Estado de PQRs")
        fig3 = px.histogram(pqrs, x="Tipo", color="Estado", barmode="group", title="Distribución de PQRs")
        st.plotly_chart(fig3, use_container_width=True)

        st.subheader("💼 Cartera por Cliente")
        fig4 = px.bar(cartera, x="Cliente", y="Saldo", color="Estado", title="Saldo pendiente")
        st.plotly_chart(fig4, use_container_width=True)

    # ==========================
    # Próximo vencimiento de PQR
    # ==========================
    st.subheader("⏳ Próximos vencimientos de PQRs")

    hoy = datetime.today()
    pqrs["Días Restantes"] = (pqrs["Fecha Vencimiento"] - hoy).dt.days
    st.dataframe(pqrs[["ID","Tipo","Usuario","Fecha Vencimiento","Estado","Días Restantes"]])


################ TAB 5: Cartera ##############################

with tab5:

    st.title("💼 Módulo de Cartera ")

    # --------------------------
    # Datos de ejemplo (mockup)
    # --------------------------
    clientes = pd.DataFrame([
        {"Cliente": "Carlos Pérez", "NIT": "900123456", "Telefono": "3001234567", "Saldo": 1200000, "Estado": "Mora"},
        {"Cliente": "María Gómez", "NIT": "800654321", "Telefono": "3109876543", "Saldo": 0, "Estado": "Corriente"},
        {"Cliente": "Juan López", "NIT": "750987654", "Telefono": "3024567890", "Saldo": 350000, "Estado": "Mora"},
        {"Cliente": "Empresa XYZ", "NIT": "901456789", "Telefono": "3152223344", "Saldo": 2000000, "Estado": "Mora"},
    ])

    facturas = pd.DataFrame([
        {"Cliente": "Carlos Pérez", "Factura": "FAC-001", "Fecha": datetime(2025,7,1), "Vencimiento": datetime(2025,7,15), "Valor": 1200000, "Pagado": 0},
        {"Cliente": "María Gómez", "Factura": "FAC-002", "Fecha": datetime(2025,7,5), "Vencimiento": datetime(2025,7,20), "Valor": 500000, "Pagado": 500000},
        {"Cliente": "Juan López", "Factura": "FAC-003", "Fecha": datetime(2025,7,10), "Vencimiento": datetime(2025,7,25), "Valor": 350000, "Pagado": 0},
        {"Cliente": "Empresa XYZ", "Factura": "FAC-004", "Fecha": datetime(2025,7,2), "Vencimiento": datetime(2025,7,16), "Valor": 2000000, "Pagado": 0},
    ])

    # --------------------------
    # Dashboard KPIs
    # --------------------------
    st.subheader("📊 Dashboard de Cartera")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("💰 Total Cartera Vencida", f"${clientes['Saldo'].sum():,.0f}")
    with col2:
        facturacion_mes = facturas["Valor"].sum()
        st.metric("📄 Facturación del Mes", f"${facturacion_mes:,.0f}")
    with col3:
        recaudo_mes = facturas["Pagado"].sum()
        st.metric("✅ Recaudo del Mes", f"${recaudo_mes:,.0f}")

    # Gráfica de cartera
    fig = px.bar(clientes, x="Cliente", y="Saldo", color="Estado", title="Cartera por Cliente")
    st.plotly_chart(fig, use_container_width=True)

    # --------------------------
    # Tabla de Clientes
    # --------------------------
    st.subheader("📋 Gestión de Clientes")
    st.dataframe(clientes, use_container_width=True)

    # Selección de cliente
    cliente_sel = st.selectbox("🔍 Seleccione un cliente para ver detalle:", clientes["Cliente"].unique())

    # --------------------------
    # Detalle Cliente
    # --------------------------
    st.subheader(f"📑 Detalle del Cliente: {cliente_sel}")

    facturas_cliente = facturas[facturas["Cliente"] == cliente_sel]
    st.dataframe(facturas_cliente, use_container_width=True)

    # --------------------------
    # Registro de Pago
    # --------------------------
    st.subheader("💵 Registrar un Pago")

    with st.form("form_pago"):
        factura_sel = st.selectbox("Factura", facturas_cliente["Factura"].unique())
        valor_pago = st.number_input("Valor del pago", min_value=0, value=0, step=50000)
        fecha_pago = st.date_input("Fecha de pago", value=datetime.today())
        medio_pago = st.selectbox("Medio de pago", ["Efectivo", "Transferencia", "PSE", "Cheque"])
        guardar = st.form_submit_button("Guardar Pago")

    if guardar:
        idx = facturas[facturas["Factura"] == factura_sel].index[0]
        facturas.at[idx, "Pagado"] += valor_pago
        st.success(f"✅ Pago de ${valor_pago:,.0f} registrado para la factura {factura_sel}")

        # Actualizar saldo cliente
        saldo_cliente = facturas[facturas["Cliente"] == cliente_sel]["Valor"].sum() - facturas[facturas["Cliente"] == cliente_sel]["Pagado"].sum()
        clientes.loc[clientes["Cliente"] == cliente_sel, "Saldo"] = saldo_cliente
        clientes.loc[clientes["Cliente"] == cliente_sel, "Estado"] = "Corriente" if saldo_cliente == 0 else "Mora"

        st.info(f"Nuevo saldo de {cliente_sel}: ${saldo_cliente:,.0f}")


