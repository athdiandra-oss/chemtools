import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import json
import os

# ==================== CONFIG ====================
st.set_page_config(
    page_title="🧪 ChemLab Mini Tools",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== TEMA MANAGEMENT ====================
if 'tema' not in st.session_state:
    st.session_state.tema = 'light'

if 'history' not in st.session_state:
    st.session_state.history = []

# Dictionary Tema
TEMA_CONFIG = {
    'light': {
        'bg_color': '#ffffff',
        'text_color': '#000000',
        'primary': '#FF6B6B',
        'secondary': '#4ECDC4',
        'accent': '#FFE66D',
        'card_bg': '#f0f2f6',
        'success_bg': '#d4edda',
        'error_bg': '#f8d7da',
    },
    'dark': {
        'bg_color': '#1e1e1e',
        'text_color': '#ffffff',
        'primary': '#FF6B9D',
        'secondary': '#00D9FF',
        'accent': '#FFD700',
        'card_bg': '#2d2d2d',
        'success_bg': '#1e4620',
        'error_bg': '#4d1f1f',
    },
    'ocean': {
        'bg_color': '#e8f4f8',
        'text_color': '#003d5c',
        'primary': '#006BA6',
        'secondary': '#0496FF',
        'accent': '#00D4FF',
        'card_bg': '#cfe9f3',
        'success_bg': '#c8e6c9',
        'error_bg': '#ffcccc',
    },
    'forest': {
        'bg_color': '#f1f5f1',
        'text_color': '#1b4332',
        'primary': '#2d6a4f',
        'secondary': '#52b788',
        'accent': '#74c69d',
        'card_bg': '#d8f3dc',
        'success_bg': '#b7e4c7',
        'error_bg': '#ffcccc',
    },
    'sunset': {
        'bg_color': '#fff5f0',
        'text_color': '#5a2c1e',
        'primary': '#ff6b35',
        'secondary': '#f7931e',
        'accent': '#fdb833',
        'card_bg': '#ffe8d6',
        'success_bg': '#d4edda',
        'error_bg': '#f8d7da',
    }
}

tema_aktif = TEMA_CONFIG[st.session_state.tema]

# ==================== HELPER FUNCTIONS ====================
def add_to_history(operation, inputs, result):
    """Add calculation to history"""
    entry = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'operation': operation,
        'inputs': inputs,
        'result': result
    }
    st.session_state.history.append(entry)

def export_history_to_csv():
    """Export calculation history as CSV"""
    if not st.session_state.history:
        return None
    df = pd.DataFrame(st.session_state.history)
    return df.to_csv(index=False)

def clear_history():
    """Clear all history"""
    st.session_state.history = []

# Custom CSS dinamis
st.markdown(f"""
    <style>
    :root {{
        --bg-color: {tema_aktif['bg_color']};
        --text-color: {tema_aktif['text_color']};
        --primary: {tema_aktif['primary']};
        --secondary: {tema_aktif['secondary']};
        --accent: {tema_aktif['accent']};
    }}
    
    * {{
        background-color: {tema_aktif['bg_color']};
        color: {tema_aktif['text_color']};
    }}
    
    .metric-card {{
        background-color: {tema_aktif['card_bg']};
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid {tema_aktif['primary']};
        color: {tema_aktif['text_color']};
    }}
    
    .success-card {{
        background-color: {tema_aktif['success_bg']};
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid {tema_aktif['secondary']};
        color: {tema_aktif['text_color']};
    }}
    
    .error-card {{
        background-color: {tema_aktif['error_bg']};
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid {tema_aktif['primary']};
        color: {tema_aktif['text_color']};
    }}
    
    .dashboard-box {{
        background-color: {tema_aktif['card_bg']};
        padding: 25px;
        border-radius: 12px;
        border: 2px solid {tema_aktif['primary']};
        margin: 10px 0;
    }}
    
    .theme-btn {{
        background-color: {tema_aktif['secondary']};
        color: white;
        padding: 10px 15px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        margin: 5px;
    }}
    
    .stButton > button {{
        background-color: {tema_aktif['primary']};
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }}
    
    </style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR - MENU & TEMA ====================
with st.sidebar:
    st.markdown("# ⚙️ CONTROL PANEL")
    
    # Selector Tema
    st.subheader("🎨 Pilih Tema")
    tema_pilihan = st.selectbox(
        "Pilih tema latar:",
        ["light", "dark", "ocean", "forest", "sunset"],
        index=["light", "dark", "ocean", "forest", "sunset"].index(st.session_state.tema),
        key="tema_select"
    )
    
    if tema_pilihan != st.session_state.tema:
        st.session_state.tema = tema_pilihan
        st.rerun()
    
    # Tampilkan preview tema
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("💡", help="Light Theme", key="light_btn"):
            st.session_state.tema = 'light'
            st.rerun()
    with col2:
        if st.button("🌙", help="Dark Theme", key="dark_btn"):
            st.session_state.tema = 'dark'
            st.rerun()
    with col3:
        if st.button("🌊", help="Ocean Theme", key="ocean_btn"):
            st.session_state.tema = 'ocean'
            st.rerun()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🌲", help="Forest Theme", key="forest_btn"):
            st.session_state.tema = 'forest'
            st.rerun()
    with col2:
        if st.button("🌅", help="Sunset Theme", key="sunset_btn"):
            st.session_state.tema = 'sunset'
            st.rerun()
    
    st.divider()
    
    # Menu Utama
    st.markdown("# 📋 MENU UTAMA")
    menu = st.selectbox(
        "Pilih Fitur",
        [
            "📊 Dashboard",
            "🏠 Beranda",
            "📐 Kalkulator Pengenceran",
            "🎮 Tebak Warna Reaksi",
            "🧠 Analisis Kesalahan Praktikum",
            "📚 Panduan & Tips"
        ]
    )
    
    st.divider()
    st.markdown("### 📌 Info Aplikasi")
    st.info("""
    **ChemLab Mini Tools v2.1**
    
    Platform pembelajaran kimia interaktif dengan:
    • 🧮 Kalkulator pengenceran
    • 🎯 Game quiz warna reaksi
    • 🔧 Troubleshooting praktikum
    • 🎨 5 tema warna berbeda
    • 📊 Riwayat perhitungan
    """)

# ==================== DASHBOARD ====================
if menu == "📊 Dashboard":
    st.title("📊 Dashboard ChemLab")
    
    # Statistik
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="dashboard-box">
            <h3>🎮 Quiz Dimainkan</h3>
            <h1>{st.session_state.get('total', 0)}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="dashboard-box">
            <h3>✅ Jawaban Benar</h3>
            <h1>{st.session_state.get('skor', 0)}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        total = st.session_state.get('total', 0)
        akurasi = (st.session_state.get('skor', 0) / total * 100) if total > 0 else 0
        st.markdown(f"""
        <div class="dashboard-box">
            <h3>📈 Akurasi</h3>
            <h1>{akurasi:.0f}%</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="dashboard-box">
            <h3>🎨 Tema Aktif</h3>
            <h1>{st.session_state.tema.upper()}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Chart statistik
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Distribusi Jawaban")
        total = st.session_state.get('total', 0)
        skor = st.session_state.get('skor', 0)
        
        if total > 0:
            try:
                fig = go.Figure(data=[
                    go.Pie(
                        labels=['Benar', 'Salah'],
                        values=[skor, total - skor],
                        marker=dict(colors=[tema_aktif['secondary'], tema_aktif['primary']])
                    )
                ])
                fig.update_layout(height=400, paper_bgcolor=tema_aktif['bg_color'], font=dict(color=tema_aktif['text_color']))
                st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"❌ Terjadi kesalahan saat membuat grafik: {str(e)}")
        else:
            st.info("📭 Belum ada data quiz. Mulai main quiz untuk melihat statistik!")
    
    with col2:
        st.subheader("📊 Riwayat Perhitungan")
        if st.session_state.history:
            st.success(f"✅ Total perhitungan: {len(st.session_state.history)}")
            
            # Show last 5 calculations
            st.write("**5 Perhitungan Terakhir:**")
            for i, entry in enumerate(reversed(st.session_state.history[-5:]), 1):
                st.write(f"{i}. {entry['timestamp']} - {entry['operation']}")
        else:
            st.info("📭 Belum ada riwayat perhitungan")
    
    st.divider()
    st.subheader("📥 Export Data")
    col1, col2 = st.columns(2)
    with col1:
        csv_data = export_history_to_csv()
        if csv_data:
            st.download_button(
                label="📥 Unduh Riwayat (CSV)",
                data=csv_data,
                file_name=f"chemlab_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                key="download_csv"
            )
    with col2:
        if st.button("🗑️ Hapus Semua Riwayat", key="clear_history_btn"):
            clear_history()
            st.success("✅ Riwayat berhasil dihapus!")
            st.rerun()

# ==================== HALAMAN BERANDA ====================
elif menu == "🏠 Beranda":
    st.title("🧪 ChemLab Mini Tools v2.1")
    st.markdown("### Selamat datang di platform pembelajaran kimia interaktif!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>📊 Kalkulator</h3>
            <p>Hitung pengenceran larutan dengan mudah menggunakan rumus M₁V₁ = M₂V₂</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>🎮 Game Quiz</h3>
            <p>Asah pengetahuan dengan tebak warna reaksi dan dapatkan skor</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>🧠 Troubleshooting</h3>
            <p>Analisis kesalahan praktikum dan temukan solusinya</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📚 Fitur Utama")
        st.markdown("""
        ✅ **Interaktif**: Belajar sambil bermain dengan interface yang user-friendly
        
        ✅ **Visualisasi**: Grafik dan chart untuk memahami konsep dengan lebih baik
        
        ✅ **Riwayat**: Simpan dan export semua perhitungan Anda
        
        ✅ **Tema Dinamis**: Pilih 5 tema warna berbeda sesuai preferensi Anda
        """)
    
    with col2:
        st.subheader("🎨 Kustomisasi Pengalaman")
        st.markdown(f"""
        ### Tema Warna Tersedia:
        - 💡 **Light** - Terang dan minimalis
        - 🌙 **Dark** - Gelap untuk mata yang nyaman
        - 🌊 **Ocean** - Biru seperti laut
        - 🌲 **Forest** - Hijau alam yang menenangkan
        - 🌅 **Sunset** - Warna hangat matahari terbenam
        
        **Pilih tema favorit Anda di sidebar!**
        """)

# ==================== KALKULATOR PENGENCERAN ====================
elif menu == "📐 Kalkulator Pengenceran":
    st.header("📐 Kalkulator Pengenceran")
    st.markdown("Gunakan rumus: **M₁V₁ = M₂V₂**")
    
    tab1, tab2, tab3 = st.tabs(["📐 Kalkulator", "📖 Panduan", "💾 Riwayat"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Input Data")
            M1 = st.number_input("Konsentrasi Awal (M1) [mol/L]", min_value=0.0, value=1.0, step=0.1)
            V1 = st.number_input("Volume Awal (V1) [mL]", min_value=0.0, value=100.0, step=10.0)
            
            pilihan_hitung = st.radio(
                "Apa yang ingin dihitung?",
                ["Volume Akhir (V2)", "Konsentrasi Akhir (M2)"]
            )
            
            if pilihan_hitung == "Volume Akhir (V2)":
                M2 = st.number_input("Konsentrasi Akhir (M2) [mol/L]", min_value=0.001, value=0.5, step=0.1, help="Nilai harus lebih besar dari 0")
                hitung_btn = st.button("🔢 Hitung V2", use_container_width=True, key="calc_v2")
                
                if hitung_btn:
                    try:
                        if M2 <= 0:
                            st.warning("⚠️ Konsentrasi akhir (M2) harus lebih besar dari 0!")
                        else:
                            V2 = (M1 * V1) / M2
                            st.success(f"✅ Hasil Perhitungan")
                            st.markdown(f"""
                            <div class="success-card">
                                <h4>✅ Hasil Perhitungan</h4>
                                <h2>V2 = {V2:.2f} mL</h2>
                                <p><strong>Arti:</strong> Encerkan {V1:.0f} mL larutan {M1} M dengan air hingga volumenya menjadi {V2:.2f} mL</p>
                                <p><strong>Air yang ditambahkan:</strong> {V2 - V1:.2f} mL</p>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Add to history
                            add_to_history(
                                "Hitung V2",
                                {"M1": M1, "V1": V1, "M2": M2},
                                {"V2": V2}
                            )
                            
                            # Visualisasi
                            fig = go.Figure()
                            fig.add_trace(go.Bar(
                                x=['Awal', 'Akhir'],
                                y=[V1, V2],
                                marker=dict(color=[tema_aktif['primary'], tema_aktif['secondary']]),
                                text=[f'{V1:.0f} mL', f'{V2:.2f} mL'],
                                textposition='auto',
                            ))
                            fig.update_layout(
                                title="Perubahan Volume",
                                height=300,
                                paper_bgcolor=tema_aktif['bg_color'],
                                plot_bgcolor=tema_aktif['card_bg'],
                                font=dict(color=tema_aktif['text_color'])
                            )
                            st.plotly_chart(fig, use_container_width=True)
                    except Exception as e:
                        st.error(f"❌ Terjadi kesalahan: {str(e)}")
            
            else:  # Hitung M2
                V2 = st.number_input("Volume Akhir (V2) [mL]", min_value=0.001, value=200.0, step=10.0, help="Nilai harus lebih besar dari 0")
                hitung_btn = st.button("🔢 Hitung M2", use_container_width=True, key="calc_m2")
                
                if hitung_btn:
                    try:
                        if V2 <= 0:
                            st.warning("⚠️ Volume akhir (V2) harus lebih besar dari 0!")
                        else:
                            M2 = (M1 * V1) / V2
                            st.success(f"✅ Hasil Perhitungan")
                            
                            dilution_ratio = M1 / M2 if M2 > 0 else float('inf')
                            dilution_text = f"{dilution_ratio:.2f}x" if dilution_ratio != float('inf') else "∞x"
                            
                            st.markdown(f"""
                            <div class="success-card">
                                <h4>✅ Hasil Perhitungan</h4>
                                <h2>M2 = {M2:.4f} mol/L</h2>
                                <p><strong>Arti:</strong> Konsentrasi larutan setelah pengenceran menjadi {M2:.4f} mol/L</p>
                                <p><strong>Tingkat pengenceran:</strong> {dilution_text}</p>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Add to history
                            add_to_history(
                                "Hitung M2",
                                {"M1": M1, "V1": V1, "V2": V2},
                                {"M2": M2}
                            )
                            
                            # Visualisasi
                            fig = go.Figure()
                            fig.add_trace(go.Bar(
                                x=['Awal', 'Akhir'],
                                y=[M1, M2],
                                marker=dict(color=[tema_aktif['primary'], tema_aktif['secondary']]),
                                text=[f'{M1:.2f} mol/L', f'{M2:.4f} mol/L'],
                                textposition='auto',
                            ))
                            fig.update_layout(
                                title="Perubahan Konsentrasi",
                                height=300,
                                paper_bgcolor=tema_aktif['bg_color'],
                                plot_bgcolor=tema_aktif['card_bg'],
                                font=dict(color=tema_aktif['text_color'])
                            )
                            st.plotly_chart(fig, use_container_width=True)
                    except Exception as e:
                        st.error(f"❌ Terjadi kesalahan: {str(e)}")
        
        with col2:
            st.subheader("📐 Rumus & Formula")
            st.info("""
            **Rumus Pengenceran:**
            
            M₁V₁ = M₂V₂
            
            Dimana:
            - M₁ = Konsentrasi awal (mol/L)
            - V₁ = Volume awal (mL)
            - M₂ = Konsentrasi akhir (mol/L)
            - V₂ = Volume akhir (mL)
            """)
            
            st.warning("""
            **💡 Tips Penting:**
            - Pastikan satuan volume konsisten
            - Pengenceran = M berkurang, V bertambah
            - Jumlah mol zat terlarut tetap sama
            """)
    
    with tab2:
        st.markdown("""
        ### 📖 Panduan Pengenceran Larutan
        
        **Apa itu pengenceran?**
        Pengenceran adalah proses menambahkan pelarut (biasanya air) ke dalam larutan untuk menurunkan konsentrasinya.
        
        **Langkah-langkah praktis:**
        1. Hitung berapa banyak larutan pekat yang dibutuhkan
        2. Hitung berapa banyak pelarut (air) yang ditambahkan
        3. Campurkan perlahan sambil diaduk
        4. Biarkan sebentar agar merata
        
        **Contoh soal:**
        - Anda punya 100 mL larutan HCl 2 M
        - Ingin membuat larutan HCl 0.5 M
        - Berapa volume akhir yang dihasilkan?
        - **Jawab:** V₂ = (2 × 100) / 0.5 = 400 mL
        """)
    
    with tab3:
        st.subheader("💾 Riwayat Perhitungan")
        if st.session_state.history:
            df_history = pd.DataFrame(st.session_state.history)
            st.dataframe(df_history, use_container_width=True)
            
            # Export button
            csv_data = export_history_to_csv()
            st.download_button(
                label="📥 Unduh Riwayat (CSV)",
                data=csv_data,
                file_name=f"calculation_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                key="download_history_csv"
            )
        else:
            st.info("💾 Belum ada riwayat perhitungan")

# ==================== TEBAK WARNA REAKSI ====================
elif menu == "🎮 Tebak Warna Reaksi":
    st.header("🎮 Tebak Warna Reaksi - Game Quiz")
    
    if 'skor' not in st.session_state:
        st.session_state.skor = 0
        st.session_state.total = 0
    
    # Soal-soal
    soal_list = [
        {
            "pertanyaan": "KMnO4 + Fe²⁺ → warna apa?",
            "pilihan": ["Ungu", "Bening", "Coklat", "Hijau"],
            "jawaban": "Bening",
            "penjelasan": "KMnO4 (ungu) tereduksi menjadi Mn²⁺ (tidak berwarna). Ungu hilang → Bening"
        },
        {
            "pertanyaan": "Ag⁺ + Cl⁻ → endapan warna?",
            "pilihan": ["Putih", "Kuning", "Biru", "Merah"],
            "jawaban": "Putih",
            "penjelasan": "AgCl membentuk endapan putih yang tidak larut dalam air"
        },
        {
            "pertanyaan": "I₂ dalam larutan → warna?",
            "pilihan": ["Merah", "Coklat", "Ungu", "Hijau"],
            "jawaban": "Coklat",
            "penjelasan": "I₂ (iodium) dalam larutan berubah menjadi warna coklat kemerahan"
        },
        {
            "pertanyaan": "CuSO4 + NaOH → endapan?",
            "pilihan": ["Putih", "Biru", "Merah", "Kuning"],
            "jawaban": "Biru",
            "penjelasan": "Cu(OH)₂ membentuk endapan biru muda"
        },
        {
            "pertanyaan": "Fe³⁺ + SCN⁻ → warna?",
            "pilihan": ["Biru", "Merah", "Hijau", "Kuning"],
            "jawaban": "Merah",
            "penjelasan": "Kompleks [Fe(SCN)]²⁺ memberikan warna merah/merah darah"
        }
    ]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Skor", st.session_state.skor)
    with col2:
        st.metric("Total Soal", st.session_state.total)
    with col3:
        if st.session_state.total > 0:
            persentase = (st.session_state.skor / st.session_state.total) * 100
            st.metric("Akurasi", f"{persentase:.0f}%")
    
    st.divider()
    
    tabs = st.tabs([f"Soal {i+1}" for i in range(len(soal_list))])
    
    for idx, (tab, soal) in enumerate(zip(tabs, soal_list)):
        with tab:
            st.subheader(f"❓ {soal['pertanyaan']}")
            
            jawaban_user = st.radio(
                "Pilih jawaban:",
                soal['pilihan'],
                key=f"soal_{idx}"
            )
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"✅ Cek Jawaban {idx+1}", use_container_width=True, key=f"check_{idx}"):
                    st.session_state.total += 1
                    
                    if jawaban_user == soal['jawaban']:
                        st.session_state.skor += 1
                        st.markdown(f"""
                        <div class="success-card">
                            <h3>🎉 Benar!</h3>
                            <p>{soal['penjelasan']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class="error-card">
                            <h3>❌ Salah!</h3>
                            <p><strong>Jawaban benar:</strong> {soal['jawaban']}</p>
                            <p><strong>Penjelasan:</strong> {soal['penjelasan']}</p>
                        </div>
                        """, unsafe_allow_html=True)
            
            with col2:
                if st.button("💡 Lihat Penjelasan", use_container_width=True, key=f"explain_{idx}"):
                    st.info(soal['penjelasan'])

# ==================== ANALISIS KESALAHAN ====================
elif menu == "🧠 Analisis Kesalahan Praktikum":
    st.header("🧠 Analisis Kesalahan Praktikum")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        masalah = st.selectbox(
            "Masalah yang terjadi:",
            [
                "Pilih masalah...",
                "❌ Larutan tidak berubah warna",
                "❌ Hasil titrasi berbeda jauh",
                "⏱️ End point terlalu cepat",
                "🧂 Kristal tidak terbentuk",
                "🫧 Gas tidak keluar"
            ]
        )
    
    with col2:
        if st.button("🔍 Analisis", use_container_width=True, key="analisis_btn"):
            st.session_state.analisis = True
    
    st.divider()
    
    if 'analisis' in st.session_state and st.session_state.analisis:
        if masalah == "Pilih masalah...":
            st.warning("Silakan pilih masalah terlebih dahulu")
        
        elif masalah == "❌ Larutan tidak berubah warna":
            st.markdown("""
            <div class="error-card">
                <h3>📋 Kemungkinan Penyebab:</h3>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                **🔴 Masalah Utama:**
                1. Indikator salah
                2. Reagen tidak bereaksi
                3. pH tidak sesuai
                """)
            
            with col2:
                st.markdown("""
                **🟡 Solusi:**
                1. Periksa jenis indikator
                2. Pastikan reagen segar
                3. Ukur pH larutan
                """)
            
            with col3:
                st.markdown("""
                **🟢 Pencegahan:**
                1. Catat tanggal kadaluarsa
                2. Simpan di tempat gelap
                3. Gunakan wadah tertutup
                """)
        
        elif masalah == "❌ Hasil titrasi berbeda jauh":
            st.markdown("""
            <div class="error-card">
                <h3>📋 Kemungkinan Penyebab:</h3>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                **🔴 Masalah Utama:**
                1. Kesalahan pembacaan buret
                2. Larutan tidak homogen
                3. Teknik pipet salah
                """)
            
            with col2:
                st.markdown("""
                **🟡 Solusi:**
                1. Baca meniskus di mata sejajar
                2. Aduk larutan dengan baik
                3. Pegang pipet vertikal
                """)
            
            with col3:
                st.markdown("""
                **🟢 Pencegahan:**
                1. Kalibrasikan alat ukur
                2. Lakukan minimal 3x titrasi
                3. Ambil rata-rata yang konsisten
                """)
        
        elif masalah == "⏱️ End point terlalu cepat":
            st.markdown("""
            <div class="error-card">
                <h3>📋 Kemungkinan Penyebab:</h3>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                **🔴 Masalah Utama:**
                1. Konsentrasi terlalu tinggi
                2. Salah perhitungan awal
                3. Alat tidak bersih
                """)
            
            with col2:
                st.markdown("""
                **🟡 Solusi:**
                1. Encerkan larutan
                2. Hitung ulang volume
                3. Cuci alat dengan baik
                """)
            
            with col3:
                st.markdown("""
                **🟢 Pencegahan:**
                1. Lakukan uji pendahuluan
                2. Gunakan pipet lebih kecil
                3. Tambahkan indikator hati-hati
                """)

# ==================== PANDUAN & TIPS ====================
elif menu == "📚 Panduan & Tips":
    st.header("📚 Panduan & Tips Belajar Kimia")
    
    tab1, tab2, tab3 = st.tabs(["📖 Teori", "🎯 Tips Praktikum", "⚗️ Reaksi Umum"])
    
    with tab1:
        st.subheader("Teori Dasar Pengenceran & Titrasi")
        st.markdown("""
        ### 1. Pengenceran Larutan
        **Pengenceran** adalah proses menambahkan pelarut untuk mengurangi konsentrasi larutan.
        
        - Mol zat terlarut tetap sama
        - Volume bertambah
        - Konsentrasi berkurang
        
        ### 2. Titrasi
        **Titrasi** adalah teknik untuk menentukan konsentrasi larutan dengan cara mereaksikannya dengan larutan standar.
        
        - Digunakan untuk analisis kuantitatif
        - Memerlukan indikator untuk menentukan end point
        - Harus dilakukan minimal 3 kali untuk hasil akurat
        """)
    
    with tab2:
        st.subheader("🎯 Tips Sukses Praktikum")
        st.markdown("""
        #### Persiapan Sebelum Praktikum
        - ✅ Baca SOP dengan teliti
        - ✅ Siapkan semua alat dan bahan
        - ✅ Periksa kondisi alat (bersih, tidak bocor)
        - ✅ Gunakan APD lengkap (jas lab, sarung tangan, kacamata)
        
        #### Selama Praktikum
        - 🔍 Amati perubahan dengan cermat
        - 📝 Catat data secara real-time
        - 🧼 Cuci alat setelah digunakan
        - 🚨 Minta bantuan jika ada yang tidak jelas
        
        #### Setelah Praktikum
        - 📊 Analisis data dengan statistik
        - 🤔 Bandingkan dengan literatur
        - 📋 Tulis laporan yang jelas dan terstruktur
        """)
    
    with tab3:
        st.subheader("⚗️ Reaksi Kimia Umum & Warnanya")
        
        data_reaksi = {
            "Reaksi": [
                "KMnO₄ (ungu) + Fe²⁺",
                "Ag⁺ + Cl⁻",
                "I₂ dalam larutan",
                "CuSO₄ + NaOH",
                "Fe³⁺ + SCN⁻",
                "K₄[Fe(CN)₆] + Fe³⁺",
                "Cu²⁺ + NH₃"
            ],
            "Warna Hasil": [
                "Bening (ungu hilang)",
                "Endapan putih",
                "Coklat kemerahan",
                "Endapan biru",
                "Merah darah",
                "Biru Prusia",
                "Biru terang"
            ],
            "Catatan": [
                "Permanganat tereduksi",
                "AgCl tidak larut",
                "Halogens berwarna",
                "Cu(OH)₂ membentuk endapan",
                "Kompleks Fe-SCN",
                "Kompleks besi sianida",
                "Kompleks ammin"
            ]
        }
        
        try:
            df_reaksi = pd.DataFrame(data_reaksi)
            st.dataframe(df_reaksi, use_container_width=True)
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan saat menampilkan tabel: {str(e)}")

st.divider()
st.markdown(f"""
<div style="text-align: center; color: {tema_aktif['text_color']}; opacity: 0.7;">
    <p>🧪 <strong>ChemLab Mini Tools v2.1</strong> | Tema: <strong>{st.session_state.tema.upper()}</strong></p>
    <p>© 2026 | Platform Pembelajaran Kimia Interaktif</p>
</div>
""", unsafe_allow_html=True)
