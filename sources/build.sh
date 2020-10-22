# source venv/bin/activate
set -e

mkdir -p ../fonts ../fonts/ttf ../fonts/ttf/static ../fonts/otf #../fonts/woff2

echo "GENERATING VFs"
VF_FILE=../fonts/ttf/Karla\[wght]\.ttf
fontmake -g Karla-Roman.glyphs -o variable --output-path $VF_FILE

rm -rf master_ufo/ instance_ufo/

echo "POST PROCESSING VFs"
gftools fix-nonhinting $VF_FILE $VF_FILE.fix
mv $VF_FILE.fix $VF_FILE

rm ../fonts/ttf/*gasp.ttf

gftools fix-dsig -f $VF_FILE
gftools fix-unwanted-tables $VF_FILE -t MVAR
# python3 gen_stat.py $VF_FILE


# echo "GENERATING TTFs"
# fontmake -g Karla-Roman.glyphs -i -o ttf --output-dir ../fonts/ttf/static

# echo "POST PROCESSING TTFs"
# ttfs=$(ls ../fonts/ttf/static/*.ttf)
# for ttf in $ttfs
# do
# 	ttfautohint $ttf "$ttf.fix";
# 	mv "$ttf.fix" $ttf;
	
# 	gftools fix-dsig -f $ttf;
    
# 	gftools fix-hinting $ttf;
#     mv "$ttf.fix" $ttf;
	
# 	#compressing for woff2
# 	fonttools ttLib.woff2 compress $ttf
    
# done

# echo "GENERATING OTFs"
# fontmake -g Karla-Roman.glyphs -i -o otf --output-dir ../fonts/otf/

# echo "POST PROCESSING OTFs"
# otfs=$(ls ../fonts/otf/*.otf)
# for otf in $otfs
# do
#     gftools fix-dsig -f $otf;
#     psautohint $otf;
# done


# echo "WOFF2 for static and vf"

# mv ../fonts/ttf/*.woff2 ../fonts/woff2
# mv ../fonts/ttf/static/*.woff2 ../fonts/woff2/static
