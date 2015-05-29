def largest_subsum(array)
    arr= array.dup
    sum = 0

    while arr.length > 1
        sum = arr[0] if arr[0] > sum
        n =  arr.shift
        arr[0] += n if n > 0
    end
    [sum, arr[0]].max
end
