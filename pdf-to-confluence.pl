#!/usr/bin/perl
use strict;
use warnings;
use REST::Client;

my ($url,$token) = @ARGV
print "$url";
print "$token";

my $rest_client = REST::Client->new();

print "Hello World";
