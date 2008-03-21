#!/bin/sh
#
# Run the complete RASP toolkit with all options set at defaults, in
# interactive mode: sentences (one per line) provided on stdin and
# results (immediately without any buffering) on stdout. An empty input
# line or eof shuts it down.
#
# Note that this mode of running RASP is not suitable for processing
# running text since it assumes each line is a single sentence, and it
# does not perform end of line and long line input preprocessing. Also,
# all options are pre-set.
#

RASP=/local/scratch/`whoami`/rasp3

arch=`arch | sed "s/i.86/ix86/"`_`uname -s | tr "[:upper:]" "[:lower:]"`

case $arch in
  sun4_sunos) awk=/usr/xpg4/bin/awk;;
  *) awk=awk;;
esac

if [ ! -d "$RASP" ]; then
  printf "%s: could not read RASP directory '%s'\n" "$0" "$RASP" > /dev/stderr
  exit 1
fi


rasp_tokenise=${rasp_tokenise:-$RASP/tokenise}
rasp_tag=${rasp_tag:-$RASP/tag}
rasp_morph=${rasp_morph:-$RASP/morph}
rasp_parse=${rasp_parse:-$RASP/scripts/rasp_parse.sh}


# Point tagger binary at our version of libdb.so

LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$RASP/tag/database/${arch}

tagout="O36"
parseopts=
wspans=
while getopts dmnp:w opt
do
     case $opt in
     d) debug="true";;
     m) tagout="O60";;
     n) ner="true";;
     p) parseopts="$OPTARG";;
     w) wspans="-w";;
     ?) echo "Usage: $0 [-d] [-m] [-n] [-p<parseopts>] [-w]";
        exit 1;;
     esac
done

$awk 'BEGIN{printf "^ "} /^[ ]*$/ {exit} {printf "%s ^ \n\n", $0; system("")}' | \
$rasp_tokenise/token.${arch} $wspans | \
$rasp_tag/${arch}/label - B1 b C1 N t$rasp_tag/auxiliary_files/slb.trn \
  d$rasp_tag/auxiliary_files/seclarge.lex \
  j$rasp_tag/auxiliary_files/unkstats-seclarge m$rasp_tag/auxiliary_files/tags.map\
  $tagout | \
$awk 'BEGIN{out=1}
    /^\^\^/  {if (!out) {printf "\n"; system("")}; out=1}
    /^\^ \^/ {if (!out) {printf "\n"; system("")}; printf "^_^ "; out=0; next}
    out      {gsub(/_/," ___"); print; system(""); next}
    {if ($0 ~ "^<w(>| ).*><w(>| ).*</w></w> ")
      {n=split($0,a,/\047>|> /)
       start=a[2]; sub(/^<w s=\047/,"",start); sub(/\047.*$/,"",start)
       end=a[n-2]; sub(/^.*e=\047/,"",end)
       line=sprintf("<w s=\047%s\047 e=\047%s\047 netype=\047phone\047>",start,end)
       for (i=3; i<=n-2; i++) {sub(/<.*$/,"",a[i]); line=line a[i] " "}
       sub(/<.*$/,"",a[n-1])
       printf "%s%s_%s</w> ",line,a[n-1],a[n]}
     else
      {if ($0 ~ /^<w(>| )/)
        {tag=$NF; $NF=""
         e1=match($0,"</w>([ ]*</w>)*[ ]*$")
         printf "%s_%s%s ",substr($0,1,e1-1),tag,substr($0,e1)}
       else
         {printf "%s_%s ",$1,$2}}}
    END{if (!out) {printf "\n"; system("")}}' | \
$rasp_morph/morpha.${arch} -actf $rasp_morph/verbstem.list | \
$awk '{gsub(/ :::/,":"); gsub(/ ___/,"_"); print; system("")}' | \
$rasp_parse $parseopts

