-- Creates index idx_name_first on table names of first letter of first name
CREATE idx_name_first ON names (name(0));
