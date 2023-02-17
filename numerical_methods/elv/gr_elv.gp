set title "Equilíbrio líquido-vapor"
set xlabel "Fração molar"
set ylabel "Temperatura"
set xrange [0.0:1.0]
set terminal pdfcairo
set output "fig_elv.pdf"
plot "data_elv_x" u 1:2 t "Ponto de bolha" w l,\
"data_elv_y" u 1:2 t "Ponto de orvalho" w l,\
"data_elv_x" u 1:2 t "Ponto de bolha" w p,\
"data_elv_y" u 1:2 t "Ponto de orvalho" w p
set output
set terminal wxt
replot