$LOAD_PATH.unshift('.')
require './severyAPI/rice-dining-master/lib/rice/dining'
require 'csv'
require 'time'

manifest = Rice::Dining.manifest
timestamp = Time.now.utc.iso8601

CSV.open('./data/diningData-'+ timestamp +'.csv', 'w') do |csv|
  manifest.locations.each do |loc|
    loc.items.each do |item|
      csv << [loc.name, loc.open?, item.name, item.allergens.map(&:id).join(' ')]
    end
  end
end
