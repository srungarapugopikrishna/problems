
data = 'aaabbbbccddeaafjsaeffefefe'
# data = 'https://onevmw-my.sharepoint.com/:x:/r/personal/tbhandare_vmware_com/_layouts/15/doc2.aspx?sourcedoc=%7B9649ba4f-ceca-4151-a9b8-26445e0e6708%7D&action=edit&activeCell=%27Feature%20Gap%20TC-s%27!E98&wdInitialSession=2a854ae6-3bff-4097-b1e4-c4f2b1d61fb2&wdRldC=1'
prev = None
count = 0
output = ''
for idx, i in enumerate(data):
    if idx == 0:
        prev = i
        count += 1
    else:
        if prev == i:
            count += 1
        else:
            output += prev+str(count)
            count = 1
    prev = i
output += prev+str(count)
print output
