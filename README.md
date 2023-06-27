# -UAS-PAA2_F55121036_ENISA-NILASARI

ALGORITMA BUBBLE SORT DAN INSERTION SORT
ANALISIS ALGORITMA UNTUK MENGEVALUASI :
Berikut analisis algorithm untuk mengevaluasi worst case, best case, dan average case untuk bubble sort dan insertion sort pada program :
1.	Worst case
   --> Bubble Sort: Worst case terjadi ketika elemen-elemen dalam array terurut secara terbalik. Dalam kasus ini, setiap pasangan elemen akan ditukar pada setiap iterasi, sehingga jumlah iterasi yang dibutuhkan adalah maksimum. Kompleksitas waktu untuk worst case Bubble Sort adalah O(n^2), di mana n adalah jumlah elemen dalam array.
--> Insertion Sort: Worst case terjadi ketika elemen-elemen dalam array terurut secara terbalik. Dalam kasus ini, setiap elemen harus disisipkan ke posisi yang paling awal dalam setiap iterasi. Kompleksitas waktu untuk worst case Insertion Sort adalah O(n^2), di mana n adalah jumlah elemen dalam array.
2. 	Best case
   --> Bubble Sort: Best case terjadi ketika elemen-elemen dalam array sudah terurut secara ascending. Dalam kasus ini, tidak ada pertukaran yang terjadi pada setiap iterasi, karena array sudah terurut dengan benar. Kompleksitas waktu untuk best case Bubble Sort adalah O(n), di mana n adalah jumlah elemen dalam array.
   -->  Insertion Sort: Best case terjadi ketika elemen-elemen dalam array sudah terurut secara ascending. Dalam kasus ini, tidak ada pergeseran yang terjadi pada setiap iterasi, karena setiap elemen sudah berada di posisi yang tepat. Kompleksitas waktu untuk best case Insertion Sort adalah O(n), di mana n adalah jumlah elemen dalam array.
3. Average case
   --> Bubble Sort: Rata-rata kasus terjadi ketika elemen-elemen dalam array tidak terurut secara terbalik atau terurut secara terbalik. Kompleksitas waktu untuk average case Bubble Sort adalah O(n^2), di mana n adalah jumlah elemen dalam array.
   --> Insertion Sort: Rata-rata kasus terjadi ketika elemen-elemen dalam array memiliki urutan acak. Kompleksitas waktu untuk average case Insertion Sort adalah O(n^2), di mana n adalah jumlah elemen dalam array.

=====================================================================================================================================================

ALGORITMA TSP (Travellinng Sales Problem) DAN Dijkstra
ANALISIS ALGORITMA UNTUK MENGEVALUASI :
Berikut analisis algorithm untuk mengevaluasi worst case, best case, dan average case untuk pada algoritma TSP (Travellinng Sales Problem) DAN Dijkstra pada program :
1.	Worst Case:
   -> TSP: Worst case pada algoritma TSP terjadi ketika grafik memiliki banyak simpul (vertices) dan setiap simpul terhubung dengan semua simpul lainnya. Dalam hal ini, kompleksitas waktu TSP akan menjadi sangat tinggi karena jumlah kemungkinan jalur yang harus dieksplorasi akan menjadi sangat besar. Sebagai contoh, dalam grafik dengan N simpul, kompleksitas waktu worst case TSP adalah O(N!).
  	--> Dijkstra: Worst case pada algoritma Dijkstra terjadi ketika setiap simpul pada grafik harus dikunjungi untuk menemukan jalur terpendek ke simpul tujuan. Dalam hal ini, kompleksitas waktu Dijkstra adalah O((V + E) log V), di mana V adalah jumlah simpul (vertices) dan E adalah jumlah tepi (edges) pada grafik
2.	Best Case:
   --> TSP: Best case pada algoritma TSP terjadi ketika grafik memiliki sedikit simpul atau hanya dua simpul. Dalam kasus ini, algoritma TSP akan mengembalikan jalur terpendek langsung antara dua simpul tersebut. Kompleksitas waktu best case TSP adalah O(1).
--> Dijkstra: Best case pada algoritma Dijkstra terjadi ketika simpul tujuan berada di sebelah simpul awal dan tidak ada simpul lain yang harus dikunjungi. Dalam hal ini, kompleksitas waktu Dijkstra adalah O(V), di mana V adalah jumlah simpul (vertices) pada grafik.
3.	Average case
   --> TSP: Average case pada algoritma TSP sangat sulit untuk dianalisis secara umum karena kompleksitasnya tergantung pada struktur dan ukuran grafik yang digunakan. Kompleksitas waktu rata-rata TSP biasanya lebih tinggi daripada best case, tetapi lebih rendah daripada worst case.
   --> Dijkstra: Average case pada algoritma Dijkstra juga sulit untuk dianalisis secara umum karena kompleksitasnya tergantung pada struktur dan ukuran grafik yang digunakan. Kompleksitas waktu rata-rata Dijkstra dapat bervariasi tergantung pada jumlah simpul dan tepi pada grafik.
