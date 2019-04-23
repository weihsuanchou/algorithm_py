    if not newPasscode in visited:
                            visited.add(newPasscode)
                            myQueue.append((newPasscode, step+1))