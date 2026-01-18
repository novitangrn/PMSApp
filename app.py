import streamlit as st
import pandas as pd

# Data Kelompok Jenis Jualan
kelompok_jualan = {
    1: "LOGAM DAN BATU MULIA (Permata, Emas, Batu Akik)",
    2: "LOGAM OLAHAN ELEKTRONIK DAN BAHAN BANGUNAN (Radio, TV, Mesin Jahit, Bahan Bangunan)",
    3: "WARTEL, KERTAS, PLASTIK, JASA, BARANG, KERAJINAN (Alat Tulis, Mainan, Foto Copy, Service)",
    4: "TEKSTIL, BAHAN KULIT (Konfeksi/Batik, Sepatu/Sandal/Tas, Kasur)",
    5: "BAHAN MAKANAN, MINUMAN, BAHAN KIMIA, TEMBAKAU (Rokok, Depot/Warung, Beras)",
    6: "PERTANIAN DAN PETERNAKAN (Buah, Daging, Ikan, Sayur Mayur)",
    7: "PELIHARAAN DAN TANAMAN HIAS (Akuarium, Ikan Hias, Burung, Pot, Pupuk)",
    8: "PERKANTORAN (untuk kondisi existing)"
}

# Data Kelas Pasar
pasar_kelas = {
    "Bendul Merisi": "II", "Gayungsari": "III", "Wonokromo Lama": "II",
    "Dukuh Kupang": "II", "Dukuh Kupang Barat": "III", "Genteng Baru": "Utama",
    "Lakarsantri": "III", "Bangkingan": "III", "Hewan Karang Pilang": "III",
    "Kembang": "I", "Kedungsari": "II", "Kedungdoro": "II", "Kupang": "I",
    "Pandegiling": "Darurat", "Kupang Gunung": "II", "Pakis": "II",
    "Wonokitri": "II", "Tunjungan Baru": "I", "Wonokromo- DTC": "Utama",
    "Bratang Bunga": "I", "Bratang Burung": "I", "Bratang inpres": "II",
    "Keputih": "III", "Gubeng Masjid": "I", "Gubeng Kertajaya": "II",
    "Kapasan": "Utama", "Aswotomo": "III", "Kertopaten": "Darurat",
    "Kendangsari": "III", "Tenggilis": "III", "Panjang Jiwo": "III",
    "Keputran Utara": "I", "Keputran Selatan": "I", "Dinoyo Tangsi": "III",
    "Bunga Kayoon": "I", "Krukah": "II", "Pacar Keling": "I",
    "Indrakila": "II", "Indrakila Darurat": "III", "Jl. Kelapa": "III",
    "Sutorejo": "III", "Pucang Anom": "I", "Rungkut Baru": "I",
    "Tambah Rejo": "Utama", "Asemrowo": "II", "Tidar": "I",
    "Tembok Dukuh": "II", "Baba'an Baru": "I", "Kebalen Barat": "Darurat",
    "Balongsari": "III", "Manukan Kulon": "III", "Banjar Sugihan": "III",
    "Blauran Baru": "Utama", "Koblen": "III", "Kepatihan": "III",
    "Dupak Bandarejo": "II", "Dupak Bangunrejo": "III", "Dupak Rukun": "II",
    "Krembangan": "II", "Pesapen": "III", "Pesapen Cikar": "III",
    "Jl Gresik PPI": "II", "Jembatan Merah": "II", "Pabean": "I",
    "Jl. Bibis": "II", "Jl. Dukuh": "Darurat", "Pecindilan": "I",
    "Kalianyar": "I", "Gembong Tebasan": "II", "Jagalan": "III",
    "Pegirian": "I", "Ampel": "III", "Sukodono": "III", "Simo": "II",
    "Simo Gunung": "III", "Simo Mulyo": "III", "Wonokusumo Wetan": "II"
}

# Data Tarif HPTU (Biaya per m² untuk 20 tahun)
# Format: {pasar_nama: {lantai: {bentuk: {kelompok: tarif}}}}
tarif_hptu = {
    "KAPASAN": {
        1: {
            "KIOS": {1: 2288000, 2: 1534000, 3: 1524000, 4: 14820000, 5: 1436000, 6: 1247000, 7: 0, 8: 2745600},
            "LOS": {1: 1966000, 2: 1338000, 3: 1329000, 4: 1294000, 5: 1256000, 6: 1098000, 7: 0, 8: 2359200}
        },
        2: {
            "KIOS": {1: 3163000, 2: 2409000, 3: 2339000, 4: 2357000, 5: 2311000, 6: 2122000, 7: 0, 8: 2471500},
            "LOS": {1: 2841000, 2: 2213000, 3: 2204000, 4: 2169000, 5: 2131000, 6: 1973000, 7: 0, 8: 2123500}
        },
        3: {
            "KIOS": {1: 2638000, 2: 1884000, 3: 1874000, 4: 1832000, 5: 1786000, 6: 1597000, 7: 0, 8: 2224500},
            "LOS": {1: 2316000, 2: 1688000, 3: 1679000, 4: 1644000, 5: 1606000, 6: 1448000, 7: 0, 8: 1911500}
        }
    },
    "Genteng": {
        1: {
            "KIOS": {1: 2288000, 2: 1534000, 3: 1524000, 4: 1482000, 5: 1436000, 6: 1247000, 7: 0, 8: 2745600},
            "LOS": {1: 1966000, 2: 1338000, 3: 1329000, 4: 1924000, 5: 1256000, 6: 1098000, 7: 0, 8: 2359200}
        },
        2: {
            "KIOS": {1: 2418000, 2: 1664000, 3: 1654000, 4: 1612000, 5: 1566000, 6: 1377000, 7: 0, 8: 2471500},
            "LOS": {1: 2096000, 2: 1468000, 3: 1459000, 4: 1424000, 5: 1386000, 6: 1228000, 7: 0, 8: 2123500}
        },
        3: {
            "KIOS": {1: 1758000, 2: 1004000, 3: 994000, 4: 952000, 5: 906000, 6: 717000, 7: 0, 8: 2224500},
            "LOS": {1: 1436000, 2: 808000, 3: 799000, 4: 764000, 5: 726000, 6: 568000, 7: 0, 8: 1911500}
        }
    },
    "Blauran": {
        1: {
            "KIOS": {1: 2288000, 2: 1534000, 3: 1524000, 4: 1482000, 5: 1436000, 6: 1247000, 7: 0, 8: 2745600},
            "LOS": {1: 1966000, 2: 13338000, 3: 1329000, 4: 1294000, 5: 1256000, 6: 1098000, 7: 0, 8: 2359200}
        },
        2: {
            "KIOS": {1: 1732000, 2: 979000, 3: 968000, 4: 926000, 5: 881000, 6: 691000, 7: 0, 8: 2471500},
            "LOS": {1: 1410000, 2: 782000, 3: 773000, 4: 738000, 5: 700000, 6: 542000, 7: 0, 8: 2123500}
        },
        3: {
            "KIOS": {1: 1691000, 2: 937000, 3: 927000, 4: 885000, 5: 839000, 6: 650000, 7: 0, 8: 2224500},
            "LOS": {1: 1369000, 2: 741000, 3: 732000, 4: 697000, 5: 659000, 6: 501000, 7: 0, 8: 1911500}
        }
    },
    "Tambahrejo": {
        1: {
            "KIOS": {1: 2288000, 2: 1534000, 3: 1524000, 4: 1482000, 5: 1436000, 6: 1247000, 7: 0, 8: 2745600},
            "LOS": {1: 1966000, 2: 1338000, 3: 1329000, 4: 1294000, 5: 1256000, 6: 1098000, 7: 0, 8: 2359200}
        },
        2: {
            "KIOS": {1: 1845000, 2: 1091000, 3: 1081000, 4: 1038000, 5: 993000, 6: 804000, 7: 0, 8: 2471500},
            "LOS": {1: 1523000, 2: 894000, 3: 886000, 4: 850000, 5: 813000, 6: 655000, 7: 0, 8: 2123500}
        }
    },
    "Wonokromo": {
        1: {
            "KIOS": {1: 2288000, 2: 1534000, 3: 1524000, 4: 1482000, 5: 1436000, 6: 1247000, 7: 0, 8: 2745600},
            "LOS": {1: 1966000, 2: 1338000, 3: 1329000, 4: 1294000, 5: 1256000, 6: 1098000, 7: 0, 8: 2359200}
        },
        2: {
            "KIOS": {1: 2288000, 2: 1534000, 3: 1524000, 4: 1482000, 5: 1436000, 6: 1247000, 7: 0, 8: 2471500},
            "LOS": {1: 1966000, 2: 1338000, 3: 1329000, 4: 1294000, 5: 1256000, 6: 1098000, 7: 0, 8: 2123500}
        }
    },
    "Kelas 1": {
        1: {
            "KIOS": {1: 1938000, 2: 1184000, 3: 1174000, 4: 1132000, 5: 1086000, 6: 897000, 7: 1067000, 8: 2325600},
            "LOS": {1: 1229000, 2: 794000, 3: 787000, 4: 758000, 5: 728000, 6: 601000, 7: 745000, 8: 1558800}
        },
        2: {
            "KIOS": {1: 1616000, 2: 988000, 3: 979000, 4: 944000, 5: 906000, 6: 748000, 7: 890000, 8: 2093500},
            "LOS": {1: 1083000, 2: 662000, 3: 656000, 4: 633000, 5: 607000, 6: 501000, 7: 596000, 8: 1403000}
        },
        3: {
            "KIOS": {1: 1294000, 2: 791000, 3: 784000, 4: 765000, 5: 725000, 6: 599000, 7: 712000, 8: 1884500},
            "LOS": {1: 865000, 2: 259000, 3: 524000, 4: 505000, 5: 485000, 6: 401000, 7: 476000, 8: 1263000}
        }
    },
    "Kelas 2": {
        1: {
            "KIOS": {1: 1616000, 2: 988000, 3: 979000, 4: 944000, 5: 906000, 6: 748000, 7: 0, 8: 1939200},
            "LOS": {1: 1083000, 2: 662000, 3: 656000, 4: 633000, 5: 607000, 6: 501000, 7: 0, 8: 1299600}
        },
        2: {
            "KIOS": {1: 1301000, 2: 795000, 3: 788000, 4: 760000, 5: 729000, 6: 602000, 7: 0, 8: 1745300},
            "LOS": {1: 1053000, 2: 644000, 3: 638000, 4: 615000, 5: 591000, 6: 488000, 7: 0, 8: 1169700}
        }
    },
    "Kelas 3": {
        1: {
            "KIOS": {1: 781000, 2: 477000, 3: 473000, 4: 456000, 5: 438000, 6: 362000, 7: 0, 8: 937200},
            "LOS": {1: 558000, 2: 341000, 3: 338000, 4: 326000, 5: 313000, 6: 258000, 7: 0, 8: 669600}
        }
    }
}

def get_tarif_category(pasar_name, kelas):
    """Menentukan kategori tarif berdasarkan nama pasar atau kelas"""
    if pasar_name.upper() in ["KAPASAN", "GENTENG", "BLAURAN", "TAMBAHREJO", "WONOKROMO"]:
        return pasar_name.capitalize()
    elif kelas == "Utama":
        # Pasar Utama menggunakan tarif khusus (bisa disesuaikan)
        return "KAPASAN"  # Default ke Kapasan untuk Utama
    elif kelas == "I":
        return "Kelas 1"
    elif kelas == "II":
        return "Kelas 2"
    elif kelas == "III":
        return "Kelas 3"
    else:
        return "Kelas 3"  # Default

def hitung_sewa(tarif_per_m2, luas, periode):
    """
    Rumus: (Biaya HPTU/tahun x Luas x 30%) + 11% (Biaya HPTU/tahun x Luas x 30%)
    """
    # Biaya HPTU per tahun (tarif adalah untuk 20 tahun)
    biaya_per_tahun = tarif_per_m2
    
    # Hitung biaya dasar (30% dari biaya per tahun x luas)
    biaya_dasar = biaya_per_tahun * luas * 0.30
    
    # Tambahkan 11% dari biaya dasar
    biaya_per_tahun = biaya_dasar + (biaya_dasar * 0.11)
    
    biaya_total_periode = biaya_per_tahun / 12 * periode
    
    return biaya_total_periode, biaya_dasar, biaya_per_tahun

# Streamlit UI
st.set_page_config(page_title="Kalkulator Harga Sewa Pasar", page_icon="🏪", layout="wide")

st.title("🏪 Kalkulator Harga Sewa Pasar")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Data Pedagang")
    nama_pedagang = st.text_input("Nama Pedagang", placeholder="Masukkan nama pedagang")
    nama_pasar = st.selectbox("Nama Pasar", sorted(pasar_kelas.keys()))
    
    # Tampilkan kelas pasar otomatis
    kelas_pasar = pasar_kelas[nama_pasar]
    st.info(f"Kelas Pasar: **{kelas_pasar}**")

with col2:
    st.subheader("Detail Stand")
    kelompok = st.selectbox("Kelompok Jenis Jualan", 
                           options=list(kelompok_jualan.keys()),
                           format_func=lambda x: f"Kelompok {x}: {kelompok_jualan[x]}")
    
    bentuk = st.radio("Bentuk Stand", ["KIOS", "LOS"])
    
    lantai = st.selectbox("Lantai", [1, 2, 3])
    
    luas = st.number_input("Luas (m²)", min_value=0.0, value=0.0, step=0.5)
    
    periode = st.selectbox("Masa Sewa (Bulan)", [1, 3, 6, 12])

st.markdown("---")

if st.button("💰 Hitung Harga Sewa", type="primary", use_container_width=True):
    if not nama_pedagang:
        st.error("⚠️ Silakan masukkan nama pedagang!")
    elif luas <= 0:
        st.error("⚠️ Silakan masukkan luas yang valid!")
    else:
        # Tentukan kategori tarif
        tarif_category = get_tarif_category(nama_pasar, kelas_pasar)
        
        # Cek apakah tarif tersedia
        if tarif_category in tarif_hptu:
            if lantai in tarif_hptu[tarif_category]:
                if bentuk in tarif_hptu[tarif_category][lantai]:
                    tarif_per_m2 = tarif_hptu[tarif_category][lantai][bentuk].get(kelompok, 0)
                    
                    if tarif_per_m2 == 0:
                        st.error("⚠️ Tarif untuk kelompok jenis jualan ini tidak tersedia!")
                    else:
                        # Hitung biaya sewa
                        biaya_total_periode, biaya_dasar, biaya_per_tahun = hitung_sewa(tarif_per_m2, luas, periode)
                        
                        # Tampilkan hasil
                        st.success("✅ Perhitungan Berhasil!")
                        
                        st.markdown("### 📊 Hasil Perhitungan")
                        
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric("Tarif per m²", f"Rp {tarif_per_m2:,.0f}")
                                               
                        with col2:
                            st.metric("💵 Total Biaya Sewa per Tahun", f"Rp {biaya_total:,.0f}")
                        
                        with col3:
                            st.metric(f"Biaya Sewa dalam {periode} Bulan", f"Rp {biaya_total_periode:,.0f}")

                        
                        st.markdown("---")
                        st.markdown("### 📝 Rincian")
                        st.write(f"**Pedagang:** {nama_pedagang}")
                        st.write(f"**Pasar:** {nama_pasar} (Kelas {kelas_pasar})")
                        st.write(f"**Jenis Jualan:** {kelompok_jualan[kelompok]}")
                        st.write(f"**Bentuk Stand:** {bentuk}")
                        st.write(f"**Lantai:** {lantai}")
                        st.write(f"**Luas:** {luas} m²")
                        
                        st.markdown("---")
                        #st.info("💡 **Catatan:** Biaya sewa dihitung dengan rumus: (Biaya HPTU/tahun × Luas × 30%) + 11% dari nilai tersebut")
                else:
                    st.error(f"⚠️ Bentuk stand '{bentuk}' tidak tersedia untuk konfigurasi ini!")
            else:
                st.error(f"⚠️ Lantai {lantai} tidak tersedia untuk pasar ini!")
        else:
            st.error(f"⚠️ Data tarif untuk pasar kategori '{tarif_category}' tidak ditemukan!")

# Footer
st.markdown("---")
st.markdown("*Aplikasi Kalkulator Harga Sewa Pasar - Berdasarkan SK PER-42 Tahun 2013*")
