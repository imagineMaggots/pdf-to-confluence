#!/usr/bin/perl
use strict;
use warnings;
# use REST::Client;

my ($url, $token) = @ARGV;
if (not defines $url)
{
  die "Keine URL angegeben\n";
}
if (defined $token)
{
  print "Save '$url' and '$token'\n";
  exit;
}

print "Fetch '$name'\n";

# my $rest_client = REST::Client->new();

print "Hello World";
