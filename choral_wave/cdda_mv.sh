dest=24

for ndx in {1..45}
do
    printf "mv track%2.2d.cdda.wav track%d.cdda.wav\n" "$ndx" "$dest"
    ((dest++))
done
