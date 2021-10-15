set title "Gas levels over the Last \\~48 Hours"
set xtics 7200 rotate by 30 offset -5.7, -2.2
set ytics
set mytics
set y2tics
set key outside below
set xlabel "Time (UTC)" offset 0.0, -1.6
set xdata time;
set format x "%F\n%TZ"
set timefmt "%Y-%m-%dT%H:%M:%SZ"
set grid xtics
set grid y2tics
set term pngcairo size 2000, 512 font ",10"

set format y "%.3f"
set format y2 "%.3f"

dat_f='/home/ghz/repos/mq_gases/data/gas_levels.2-3_day'
out_d='/home/ghz/repos/mq_gases/plots/'

set ylabel "AD Votlage (V)"
set y2label "AD Votlage (V)"
set output out_d.'mq-136.png'
plot dat_f using 1:3 title 'MQ-136 - H_2S' with lines lw 2 linecolor rgb "#0000ff"

set output out_d.'mq-2.png'
plot dat_f using 1:6 title 'MQ-2 - Methane, Butane, LPG, Smoke' with lines lw 2 linecolor rgb "#00ff00"

set output out_d.'mq-8.png'
plot dat_f using 1:9 title 'MQ-8 - H_2' with lines lw 2 linecolor rgb "#ff0000"

set output out_d.'mq-135.png'
plot dat_f using 1:12 title 'MQ-135 - Air Quality (Benzene, Alcohol, Smoke)' with lines lw 2 linecolor rgb "#00ffff"

set output out_d.'mq-7.png'
plot dat_f using 1:15 title 'MQ-7 - CO' with lines lw 2 linecolor rgb "#ff00ff"

set output out_d.'all_gasses.png'
plot dat_f using 1:3 title 'MQ-136 - H_2S' with lines lw 2 linecolor rgb "#0000ff", \
dat_f using 1:6 title 'MQ-2 - Methane, Butane, LPG, Smoke' with lines lw 2 linecolor rgb "#00ff00", \
dat_f using 1:9 title 'MQ-8 - H_2' with lines lw 2 linecolor rgb "#ff0000", \
dat_f using 1:12 title 'MQ-135 - Air Quality (Benzene, Alcohol, Smoke)' with lines lw 2 linecolor rgb "#00ffff", \
dat_f using 1:15 title 'MQ-7 - CO' with lines lw 2 linecolor rgb "#ff00ff"