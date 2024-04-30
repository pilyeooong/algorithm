servers = 2
sticky = false
requests = [1,2,3,4,1,1]

def round_robin(servers, sticky, requests)
  loads = []
  servers.times do
    loads.append(Array.new {[]})
  end

  session = Hash.new {[]} if sticky

  requests.each_with_index do |request, idx|
    if session and session.key?(request)
      server_idx = session[request]
    else
      server_idx = idx % servers
      session[request] = server_idx if session
    end
      loads[server_idx].append(request)
  end

  loads
end

result = round_robin(servers, sticky, requests)
p result

a,b = 1,2
b,a = a,b

p a
p b