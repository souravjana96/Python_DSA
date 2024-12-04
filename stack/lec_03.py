def useSideLane(trucks):
    st = []
    exp_truck_no = 1
    for ele in trucks:
        st.append(ele)
        while st and st[-1] == exp_truck_no:
            st.pop()
            exp_truck_no += 1
        
    return not st

trucks = [ 4, 5, 1, 2, 3]

print(useSideLane(trucks))