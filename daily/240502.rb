servers = 2
sticky = true
requests = [1,2,3,4,1,1]

def round_robin(servers ,sticky, requests)
  loads = []
  servers.times { loads.append([]) }

  if sticky
    session = {}
    requests.each_with_index do |request, idx|
      if session.key?(request)
        server_idx = session[request]
      else
        server_idx = idx % servers
        session[request] = server_idx
      end
      loads[server_idx].append(request)
    end
  else
    requests.each_with_index do |request, idx|
      server_idx = idx % servers
      loads[server_idx].append(request)
    end
  end

  loads
end

res = round_robin(servers, sticky, requests)
p res

def quick_sort(list, start, last)
  return if start >= last

  pivot = start
  left = start + 1
  right = last

  while left <= right
    while left <= last and list[left] <= list[pivot]
      left += 1
    end

    while right > start and list[right] >= list[pivot]
      right -= 1
    end

    if left > right
      list[pivot], list[right] = list[right], list[pivot]
    else
      list[left], list[right] = list[right], list[left]
    end
  end

  quick_sort(list, start, right - 1)
  quick_sort(list, right + 1, last)

  list
end

l = [5,4,2,1,7,3,6]
sorted_l = quick_sort(l, 0, l.length - 1)
p sorted_l
