# Table volunteer_assignments {
#   id int [pk, increment]
#   volunteer_id int [ref:> volunteer_profiles.id]
#   child_id int [ref:> child_profiles.id, null] // optional, if tied to a specific child
#   organization_id int [ref:> organizations.id, null]
#   role_description text
#   start_date date
#   end_date date
#   created_at datetime
#   is_deleted boolean [default: false]  
#   archived_at datetime
# }


