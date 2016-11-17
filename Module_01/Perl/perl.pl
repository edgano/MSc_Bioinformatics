#!/usr/bin/perl
use Switch;
use List::Util qw( min );
use List::Util qw( max );

switch ($ARGV[0]) {
	case "-chomp"			{chomp01();}		#1. -chomp	-input	input_file.fasta
	case "-name_find"		{name02();}			#2. -name_find	-name pepe -input	input_file.fasta
	case "-getIds"			{get03();}			#3. -getIds -input	input_file.fasta
	case "-max_exon_list"	{max04();}			#4. -max_exon_list	-input	input_file.bed	
	case "-top_exon"		{top05();}			#5. -top_exon -input	input_file.fasta -top	10
	case "-randomfasta"		{random06();}		#6. -randomfasta -sequences 10 -nucleotides	100
	case "-id"				{id07();}			#7. -id	bcra1	-input	input_file.fasta
	case "-palindrome"		{palindrome08();}	#8. -palindrome	-input	input_file.fasta
	else					{ print "previous case not true" }
}

sub chomp01 {	#print $ARGV[2],"\n";
	open(my $fh, "<", $ARGV[2]) or die "Can't open the file!";
	my $seq = "";
	my $first = 1;
	while (my $row = <$fh>) {
		if($row =~ m/^>(.*)/){
			if (!$first){									#to avoid print the previous seq for the 1st line
				print "$seq\n";								#print the seq before
				$seq="";
			}												#ini seq string
			my ($seqname, $seqinfo) = split / /,  $row, 2; 	#split by 'space' the $row variable. Split in 2 subs
			print "$seqname\n";								#print seqname of actually seq
			$first=0;			
		}else{
			chomp($row);									#delte \n
			$seq .= $row;									#adding sequences
		}
	}
	print "$seq\n";											#print last seq
	}

sub name02 {	#print $ARGV[2]," * ",$ARGV[4],"\n";
	my ($name) = uc $ARGV[2];
	open(PROTEIN, "<",$ARGV[4]) or die "Can't open the file!";
	while(my $line=<PROTEIN>){
		if($line =~ m/^>(.*)/){
		 	($seqname, $seqinfo) = split / /,  $line, 2;
		}
		if($line =~ /$name/){
			print "result: $seqname\n";
		}
	}
}

sub get03 {		#print $ARGV[2],"\n";
	open(FASTA, "<",$ARGV[2]) or die "Can't open the file!";
	while(my $line=<FASTA>){
		if($line =~ m/^>(.*)/){
		 	($seqname, $seqinfo) = split / /,  $line, 2;
		 	print "$seqname \n";
		}
	}
}

sub max04 {		#print $ARGV[2],"\n";
	open(BED, "<",$ARGV[2]) or die "Can't open the file!";

	while($line=<BED>){
		@var = split (/\t/,  $line);
		@col = split (/,/, $var[10]);
		my $min = min @col;
		print "$min\n";
	}
}

sub top05 {		#print $ARGV[2]," **** ",$ARGV[4],"\n";
	open(BED, "<",$ARGV[2]) or die "Can't open the file!";
	my @exons =();
	$i=0;		#var para el index in while
	$max = $ARGV[4] -1;
	while($line=<BED>){
		@var = split (/\t/,  $line);
		$exons[$i][0] = $var[3];
		$exons[$i][1] = max(split (/,/, $var[10]));
		$i=$i+1;
	}
	@filtered = sort { $b->[1] <=> $a->[1] } @exons;

	for (my $i=0; $i <= $max; $i++) {
	   print "$filtered[$i][0] - $filtered[$i][1]\n";
	}
}

sub random06 {	#print $ARGV[2]," **** ",$ARGV[4],"\n";
	my $outfile = "nuevo.fasta";
	my $numberSeq = $ARGV[2];
	my $numberNucleo = $ARGV[4];
	my @chars=('A','C','G','T','N');

	open(MYFILE, ">>$outfile") or die "Can't open the $outfile!\n";
	for (my $i=1; $i <= $numberSeq; $i++) {
	   print MYFILE ">sequence$i\n";
	   my $random_string;
	   foreach (1..$numberNucleo) {
			$random_string.=$chars[rand @chars];
		}
		print MYFILE "$random_string\n";
	}
	close (MYFILE)
	print "File ",$outfile," generated\n";
}

sub id07 {
  print $ARGV[1];
}

sub palindrome08 {	#print $ARGV[2];
	open(FASTA, "<",$ARGV[2]) or die "Can't open the file!";
	%data = ();
	my @palindromes = ();
	@names = ();
	my $maxElements=10;
	$re = qr/((.)(?:(??{$re})|.?)\2)/;
	while($_=<FASTA>){
		if($_ =~ m/^>(.*)/){
		 	($seqname, $seqinfo) = split / /,  $_, 2;
		}else{
			chomp($_);
			push @palindromes, "$1" while (/(?=$re)/g); #save all palindromes in a list
			foreach $pali (@palindromes){
				if(length($pali)>=6){	#if palindrome is >6
			    	if (!grep( /^$seqname$/, @names)) {
						push @names, "$seqname";
					}
			    	if(exists($data{$pali})){	#if it exists add 1 to the value
					   $data{$pali} += 1;
					}
					else{
					   $data{$pali} = 1;	# add a new key to the dictionary
					}
				}
			}
		}
	}
	$i=0;
	foreach my $name (sort { $data{$b} <=> $data{$a} } keys %data) {
	    if($i<$maxElements){
	    	printf "%-8s %s\n", $name, $data{$name};
	    	$i++;
	    }
	}
	print "**** SEQNAMES **** \n";
	print join(", ", @names),"\n";
}
