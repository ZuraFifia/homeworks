if (touchedBase and
    touchesPan == 0) then
    local x1,y1 = b [1]
    :getLinearVelocity()
    local x2,y2 = b[#b]
    :getLinearVelocity()
    if (abs(x1) + abs(x2)
        abs(y1) + abs(y2)
        0.5) and gamePhase
        == "playing" then
        for a = 1,#b do
            b[a].linearDampi
            ng = 100
        end

        print ("VICTORY")      
        gamePhase = "none"
        timer.
            performWithDelay
            (500, win)
    end
end























