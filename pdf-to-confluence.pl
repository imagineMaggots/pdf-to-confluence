#!/usr/bin/perl
use strict;
use warnings;
use REST::Client;

my $pdf = <STDIN>;
print("$pdf");

my $rest_client = REST::Client->new();

print("Hello World");
