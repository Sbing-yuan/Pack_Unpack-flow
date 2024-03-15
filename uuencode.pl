#!/usr/local/bin/perl -w                                                                                                                                                              
#=========================================================================================
# Rivision History:
# Date          By              Ext.    Version         Revision History
#-----------------------------------------------------------------------------------------
# 2024.03.06    John She        xxxx    First           Replacement for uuencode in linux
#=========================================================================================
use Term::ANSIColor;

sub showUsage {	print colored("Usage: perl $0 [INFILE] REMOTEFILE \n", 'green'),
			      "Example: perl $0 xlsx_report.tar.gz xlsx_report.tar.gz\n"}

if ($#ARGV < 1) {
   showUsage();
   exit 0;
}

open (FH, $ARGV[0]) || die "ERROR: can not read $ARGV[0]\n";
binmode(FH);

my $t;my $bindat="";
while(read(FH,$t,1000)) { 
    $bindat.=$t;
}
close FH;

print "begin 644 $ARGV[1]\n";
print (pack 'u', $bindat);
print "`\nend\n";
# end of uuencode.pl
