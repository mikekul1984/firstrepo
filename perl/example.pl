#!/usr/bin/perl

$needToFind = "bbb";
$_ = "AAAA bbb CCCC";
print "Found bbb\n" if m/$needToFind/;
