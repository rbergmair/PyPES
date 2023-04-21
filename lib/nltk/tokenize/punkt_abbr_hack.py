# -*-  coding: ascii -*-  # # # # # # # # # # # # # # # # # # # # # # # # # #

ABBRVS = {
    "Gov.", "MM.", "Mme.", "Mr.", "Ms.", "Mrs.", "Miss.", "Capt.", "Col.",
    "Dr.", "Drs.", "Rev.", "Prof.", "Sgt.", "Sr.", "St.", "Jr.", "jr.",
    "Lt.", "Gen.", "Sen.",
    "Co.", "Corp.", "Inc.",
    "cf.", "eg.", "etc.", "ex.", "ie.", "viz.", "vs.",
    "Jan.", "Feb.", "Mar.", "Apr.", "Jun.", "Jul.", "Aug.", "Sep.",
    "Oct.", "Nov.", "Dec.",
    "Ed.", "Eds.", "repr.", "Rep.", "Dem.", "trans.", "Vol.", "Vols.",
    "p.", "pp.", "rev.", "est.",
    "Fig.", "fig.", "Figs.", "figs.", "No.", "no.", "Nos.", "nos.",
    "eq.", "Eq.", "eqs.", "Eqs.", "ref.", "Ref.", "refs.", "Refs.",
    "ch.", "Ch.", "chs.", "Chs.", "sec.", "Sec.", "secs.", "Secs.",
    "dept.", "Dept.", "Univ.",
    "mol.", "Mol.", "cell.", "Cell.", "chem.", "Chem.", "biol.", "Biol.",
    "et al." 
  };

def punkt_abbr_hack( params ):
  
  for abbrv in ABBRVS:
    if abbrv[ -1 ] == ".":
      abbrv = abbrv[ :-1 ];
    abbrv = abbrv.lower();
    params.abbrev_types.add( abbrv );
  
  return params;
