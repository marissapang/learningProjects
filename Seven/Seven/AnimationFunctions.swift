//
//  AnimationFunctions.swift
//  Seven
//
//  Created by apple on 6/14/20.
//  Copyright © 2020 KnowledgeIsBacon. All rights reserved.
//

import UIKit

func moveAllTiles(dimensions: Int, tileViewBoard : Gameboard<TileView?>, tileAnimationBoard : Gameboard<UIViewPropertyAnimator>) ->
Gameboard<UIViewPropertyAnimator>{
    var tileView : TileView?
    var animator : UIViewPropertyAnimator
    var newTileAnimationBoard = tileAnimationBoard
    
    
    
    for i in 0..<dimensions {
        for j in 0..<dimensions {
            tileView = tileViewBoard[i,j]
            
            if let view = tileView {
                animator = UIViewPropertyAnimator(duration: 1, curve: .easeInOut, animations: {
                    view.transform = CGAffineTransform(translationX: 50, y: 50)})
                
                newTileAnimationBoard[i,j] = animator
            }
        }
    }
    return newTileAnimationBoard
}
