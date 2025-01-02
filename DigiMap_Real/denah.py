#%%
import folium

def tampilkan_denah():
    print("="*70)
    print("Denah UPI Cibiru".center(70))
    print("="*70)
    print("Denah telah dibuat dan disimpan sebagai 'upi_cibiru.html'\n")
    upi_cibiru = folium.Map(location = [-6.939787174459237, 107.72529789772535],
                            zoom_start = 20)
    
    #%%
    #gedung biru
    folium.Marker(location=[-6.9399425152555585, 107.72534900869695],
                tooltip='Gedung Biru',
                popup = folium.Popup(
                    """
                    <img src="denah/gedung biru.jpg" alt="Gedung Biru" style="max-width:100%;max-height:100%">
                    <h4>Gedung Biru</br>
                    </h4>
                    <h5>Deskripsi Gedung Biru</h5>
                    """, max_width=500)).add_to(upi_cibiru)

    #%%
    #gedung b
    folium.Marker(location=[-6.9398935470527565, 107.72505349878351],
                tooltip='Gedung B',
                popup = folium.Popup(
                    """
                    <img src="denah/gedung b.jpg" alt="Gedung B" style="max-width:100%;max-height:100%">
                    <h4>Gedung B</br>
                    </h4>
                    <h5>Deskripsi Gedung B</h5>
                    """, max_width=500)).add_to(upi_cibiru)

    #%%
    #kantin
    folium.Marker(location=[-6.94017260869488, 107.72448379263692],
                tooltip='Kantin',
                popup = folium.Popup(
                    """
                    <img src="denah/kantin.jpg" alt="Kantin" style="max-width:100%;max-height:100%">
                    <h4>Kantin</br>
                    </h4>
                    <h5>Deskripsi Kantin</h5>
                    """, max_width=500)).add_to(upi_cibiru)

    # %%
    # Pos Keamanan
    folium.Marker(location=[-6.940211120237557, 107.72558568149186],
                tooltip='Pos Keamanan 1',
                popup = folium.Popup(
                    """
                    <img src="denah/pos 1.jpg" alt="Pos Keamanan" style="max-width:100%;max-height:100%">
                    <h4>Pos Keamanan</br>
                    </h4>
                    <h5>Deskripsi Pos Keamanan</h5>
                    """, max_width=500)).add_to(upi_cibiru)

    # %%
    # Lab PGSD dan PGPAUD
    folium.Marker(location=[-6.93955247781857, 107.72451172048002],
                tooltip='Lab PGSD dan PGPAUD',
                popup = folium.Popup(
                    """
                    <img src="denah/lab pgsd pgpaud.jpg" alt="Lab PGSD dan PGPAUD" style="max-width:100%;max-height:100%">
                    <h4>Lab PGSD dan PGPAUD</br>
                    </h4>
                    <h5>Deskripsi Lab PGSD dan PGPAUD</h5>
                    """, max_width=500)).add_to(upi_cibiru)

    #%%
    #Lapangan Olahraga
    folium.Marker(location=[-6.939950775139731, 107.72441210966787],
                tooltip='Lapangan Olahraga',
                popup = folium.Popup(
                    """
                    <img src="denah/lapangan.jpg" alt="Lapangan Olahraga" style="max-width:100%;max-height:100%">
                    <h4>Lapangan Olahraga</br>
                    </h4>
                    <h5>Deskripsi Lapangan Olahraga</h5>
                    """, max_width=500)).add_to(upi_cibiru)

    #%%
    #Teater Terbuka
    folium.Marker(location=[-6.9394995951485905, 107.72562940552577],
                tooltip='Teater Terbuka',
                popup = folium.Popup(
                    """
                    <img src="denah/teater terbuka.jpg" alt="Teater Terbuka" style="max-width:100%;max-height:100%">
                    <h4>Teater Terbuka</br>
                    </h4>
                    <h5>Deskripsi Teater Terbuka</h5>
                    """, max_width=500)).add_to(upi_cibiru)

    #%%
    #Asrama Putri
    folium.Marker(location=[-6.93912489082591, 107.72408346465077],
                tooltip='Asrama Putri',
                popup = folium.Popup(
                    """
                    <img src="denah/asrama putri.jpg" alt="Asrama Putri" style="max-width:100%;max-height:100%">
                    <h4>Asrama Putri</br>
                    </h4>
                    <h5>Deskripsi Asrama Putri</h5>
                    """, max_width=500)).add_to(upi_cibiru)

    #%%
    #Masjid As-Sakinah
    folium.Marker(location=[-6.940078282450142, 107.72410185731447],
                tooltip='Masjid As-Sakinah',
                popup = folium.Popup(
                    """
                    <img src="denah/masjid.jpg" alt="Masjid As-Sakinah" style="max-width:100%;max-height:100%">
                    <h4>Masjid As-Sakinah</br>
                    </h4>
                    <h5>Deskripsi Masjid As-Sakinah</h5>
                    """, max_width=500)).add_to(upi_cibiru)

    #%%
    #Pos Keamanan 2
    folium.Marker(location=[-6.940291032506306, 107.72442258464262],
                tooltip='Pos Keamanan 2',
                popup = folium.Popup(
                    """
                    <img src="denah/pos 2.jpg" alt="Pos Keamanan 2" style="max-width:100%;max-height:100%">
                    <h4>Pos Keamanan 2</br>
                    </h4>
                    <h5>Deskripsi Pos Keamanan 2</h5>
                    """, max_width=500)).add_to(upi_cibiru)
    
 #%%
    upi_cibiru.save('upi_cibiru.html')
    #upi_cibiru
