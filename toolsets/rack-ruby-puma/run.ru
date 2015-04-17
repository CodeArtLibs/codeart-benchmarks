require 'rack'
require 'json'


RESPONSE_JSON = {
    :username => 'codeart',
    :permissions => ['create', 'update', 'list', 'read', 'delete'],
    :groups => {'group1' => 'crlud', 'group2' => 'cr', 'group3' => 'crlu'},
}


module CodeArtBenchmarks
    Ruby = lambda do |env|
        content_type, body = case env['PATH_INFO']
            when '/json-response'
                ['200', {'Content-Type' => 'application/json; charset=utf-8'}, [RESPONSE_JSON.to_json]]
            else
                ['200', {'Content-Type' => 'plain/text'}, ['404']]
        end
    end
end

run CodeArtBenchmarks::Ruby
