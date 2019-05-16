dir="/Users/mirkovelimirovic/Documents/GitHub/karmilla/fonts"

ttfs="$(ls $dir/*/*.ttf)"
echo $ttfs

for ttf in $ttfs; do
    woff_compress $ttf
    echo "Build woff for $ttf"
done
